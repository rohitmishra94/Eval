def instructions_following(prompt,response): 
  return  f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by AI models.
We will provide you with the user input and an AI-generated responses.
You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will assign the response a rating following the Rating Rubric and Evaluation Steps. Give step-by-step explanations for your rating, and only choose ratings from the Rating Rubric.

# Evaluation
## Metric Definition
You will be assessing model's the ability to follow instructions provided in the user prompt.

## Criteria
Instruction following: The response demonstrates a clear understanding of the instructions in the user prompt, satisfying all of the instruction's requirements.

## Rating Rubric
5: (Complete fulfillment). Response addresses all aspects and adheres to all requirements of the instruction. The user would feel like their instruction was completely understood.
4: (Good fulfillment). Response addresses most aspects and requirements of the instruction. It might miss very minor details or have slight deviations from requirements. The user would feel like their instruction was well understood.
3: (Some fulfillment). Response does not address some minor aspects and/or ignores some requirements of the instruction. The user would feel like their instruction was partially understood.
2: (Poor fulfillment). Response addresses some aspects of the instruction but misses key requirements or major components. The user would feel like their instruction was misunderstood in significant ways.
1: (No fulfillment). Response does not address the most important aspects of the instruction. The user would feel like their request was not at all understood.

## Evaluation Steps
STEP 1: Assess instruction understanding: Does the response address the intent of the instruction such that a user would not feel the instruction was ignored or misinterpreted by the response?
STEP 2: Assess requirements adherence: Does the response adhere to any requirements indicated in the instruction such as an explicitly specified word length, tone, format, or information that the response should include?

# User Inputs and AI-generated Response
## User Inputs
### Prompt
{prompt}

## AI-generated Response
{response}
"""