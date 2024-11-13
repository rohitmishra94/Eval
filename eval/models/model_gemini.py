import logging
from tenacity import retry, wait_random_exponential, stop_after_attempt
from tqdm import tqdm
from dotenv import load_dotenv
import os
from typing import Any, Dict
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import StreamingResponse
import logging_config  
from prompts.prompt_config import pairwise_prompt_selector, pointwise_prompt_selector
import google.generativeai as genai



load_dotenv()

router = APIRouter()

logger = logging.getLogger(__name__)

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                }

@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(3))
async def generate_response(params: Dict[str, Any]):
    """Generate response using OpenAI API with error handling and logging."""
    try:
        logger.info(f"Generating response with model: {params.get('model')}")
        
        model = genai.GenerativeModel(params.get('model'))
        sys_prompt = params.get('sys_prompt')
        stream = params.get('stream')
        generation_config = params.get('generation_config')
        response = await model.generate_content_async(sys_prompt,stream=stream,generation_config=generation_config)
        
        # Streaming the response
        async for chunk in response:
            if chunk.text:
                yield chunk.text  # yield each chunk's content part

        logger.info("Response generated successfully")

    except Exception as e:
        logger.error(f"Error generating response: {str(e)}", exc_info=True)
        yield "Sorry for inconvenience. Please contact support."

@router.post("/judge/pointwise")
async def judge_pointwise(request: Request):
    """Judge pointwise prompt."""
    data = await request.json()
    prompt = data.get('prompt')
    response = data.get('response')
    metric = data.get('metric')
    history = data.get('history')

    if metric not in pointwise_prompt_selector.keys():
        async def error_stream():
            yield f"Invalid metric: {metric}. Please provide a valid metric."
        return StreamingResponse(error_stream(), media_type="text/event-stream")


    if not metric.startswith('multi'):
        system_prompt = pointwise_prompt_selector[metric](prompt, response)
    else:
        system_prompt = pointwise_prompt_selector[metric](prompt, response, history)

    
    params = {
        "model": "gemini-1.5-pro",
        "sys_prompt": system_prompt,
        "stream": True,
        "generation_config": generation_config,
    }

    return StreamingResponse(content=generate_response(params), media_type="text/event-stream")


@router.post("/judge/pairwise")
async def judge_pairwise(request: Request):
    """Judge pairwise prompt."""
    data = await request.json()
    prompt = data.get('prompt')
    baseline_model_response = data.get('baseline_model_response')
    response = data.get('response')
    metric = data.get('metric')
    history = data.get('history')
    if metric not in pairwise_prompt_selector.keys():
        async def error_stream():
            yield f"Invalid metric: {metric}. Please provide a valid metric."
        return StreamingResponse(error_stream(), media_type="text/event-stream")


    if not metric.startswith('multi'):
        system_prompt = pairwise_prompt_selector[metric](prompt, baseline_model_response, response)
    else:
        system_prompt = pairwise_prompt_selector[metric](history, prompt, baseline_model_response, response)

    params = {
        "model": "gemini-1.5-pro",
        "sys_prompt": system_prompt,
        "stream": True,
        "generation_config": generation_config,
    }
    
    return StreamingResponse(content=generate_response(params),media_type="text/event-stream")


