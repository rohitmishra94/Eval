def fluency(prompt,response): 
  return  f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by AI models.
We will provide you with the user input and an AI-generated responses.
You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will assign the response a rating following the Rating Rubric and Evaluation Steps. Give step-by-step explanations for your rating, and only choose ratings from the Rating Rubric.

# Evaluation
## Metric Definition
You will be assessing fluency, which measures language mastery of the model's response based on the user prompt.

## Criteria
Fluency: The text is free of grammatical errors, employs varied sentence structures, and maintains a consistent tone and style, resulting in a smooth and natural flow that is easy to understand.

## Rating Rubric
5: (Completely fluent). The response is free of grammatical errors, demonstrates nuanced word choice, and has a natural, seamless flow.
4: (Mostly fluent). The response has very few, if any, minor grammatical errors. Word choice is clear, and sentences generally flow well.
3: (Somewhat fluent). The response has grammatical errors present, which may cause some difficulty for the reader. Word choice is mostly appropriate, but some awkward phrasing or word repetition may exist.
2: (Somewhat inarticulate). The response has frequent grammatical errors make the writing difficult to understand. Sentence structure is often awkward, and there's little sense of flow.
1: (Inarticulate). The response is riddled with grammatical issues, rendering it incomprehensible in parts. Word choices may be very limited or inaccurate.

## Evaluation Steps
STEP 1: Assess grammar correctness: Identify any specific errors in the response's sentence structure, verb usage, subject-verb agreement, punctuation, and capitalization.
STEP 2: Assess word choice and flow: Examine the response's sentence structure and how the writing moves from one idea to the next. Are words accurate and well-suited to the context?
STEP 3: Assess overall cohesion: Does the entire response read logically and smoothly, with appropriate transitions?

# User Inputs and AI-generated Response
## User Inputs
### Prompt
{prompt}

## AI-generated Response
{response}
"""

