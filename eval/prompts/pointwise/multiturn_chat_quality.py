def multiturn_chat_quality(prompt,response,history):  # type: ignore
  return  f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of responses generated by AI models in a multi-turn chat setting. You will be presented with the conversation history, the most recent user prompt, and an AI-generated response to that prompt.
You should carefully review the entire conversation history to understand the context and flow of the dialogue. Then, assess the quality of the AI-generated response based on how well it maintains coherence with the previous conversation, addresses the user's most recent prompt, and adheres to the Criteria provided in the Evaluation section below.
You will assign the response a score from 5, 4, 3, 2, 1, following the Rating Rubric and Evaluation Steps. Give step-by-step explanations for your scoring, and only choose scores from 5, 4, 3, 2, 1.

# Evaluation
## Metric Definition
You will be assessing Multi-turn Chat Quality, which measures how effectively the AI-generated response contributes to a meaningful, coherent, and engaging conversation, considering factors like context fluency, groundedness, and conciseness.

## Criteria Definition
Coherence: The response presents ideas in a logical and organized manner, with clear transitions and a consistent focus, making it easy to follow and understand.
Fluency: The text flows smoothly and naturally, adhering to grammatical rules and using appropriate vocabulary.
Instruction following: The response demonstrates a clear understanding of the task instructions, satisfying all of the instruction's requirements.
Groundedness: The response contains information included only in the context. The response does not reference any outside information.
Verbosity: The response is appropriately concise, providing sufficient detail without using complex language to thoroughly address the prompt without being overly wordy or excessively brief.
Collaborativity: The response actively contributes to the conversation by asking relevant follow-up questions, making suggestions, or offering insights when appropriate.
Recall: The response demonstrates a clear understanding of the previous conversation, referencing and utilizing relevant information from earlier turns.

## Rating Rubric
5: (Very good). Exceptionally collaborative, demonstrating excellent recall, appropriate verbosity, and strong adherence to instructions. Fully grounded in the conversation context.
4: (Good). Collaborative, with good recall, appropriate verbosity, and mostly adheres to instructions. Mostly grounded in the conversation context, with minor inconsistencies.
3: (Ok). Somewhat collaborative, demonstrating adequate recall and verbosity. Partially fulfills instructions and may contain minor ungrounded information.
2: (Bad). Lacks collaborativity, struggles with recall and verbosity. Fails to adhere to instructions and may include significant ungrounded information.
1: (Very bad). Non-collaborative, demonstrates poor recall and verbosity. Completely disregards instructions and contains substantial ungrounded information.

## Evaluation Steps
STEP 1: Carefully review the entire conversation history to gain a comprehensive understanding of the context and flow of the dialogue.
STEP 2: Assess the response in aspects of all criteria provided . Provide assessment according to each criterion.
STEP 3: Score based on the rating rubric. Give a brief rationale to explain your evaluation considering each individual criterion and the overall contribution to the conversation.

# User Inputs and AI-generated Response
## User Inputs

### Conversation History
{history}

### Current User Prompt
{prompt}

## AI-generated Response
{response}
"""
