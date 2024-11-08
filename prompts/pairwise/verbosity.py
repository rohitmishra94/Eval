# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by two AI models. We will provide you with the user input and a pair of AI-generated responses (Response A and Response B).
You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will first judge responses individually, following the Rating Rubric and Evaluation Steps.
Then you will give step-by-step explanations for your judgment, compare results to declare the winner based on the Rating Rubric and Evaluation Steps.

# Evaluation
## Metric Definition
You will be assessing the verbosity of each model's response, which measures its conciseness and ability to provide sufficient detail without being overly wordy or excessively brief.

## Criteria
Verbosity: The response is appropriately concise, providing sufficient detail without using complex language to thoroughly address the prompt without being overly wordy  or excessively brief.

## Rating Rubric
"A": Response A is more appropriately concise than Response B. It strikes a better balance between providing sufficient detail and avoiding unnecessary wordiness or excessive brevity.
"SAME": Response A and B are equally concise. They both strike the same level of balance between providing sufficient detail and avoiding unnecessary wordiness or excessive brevity.
"B": Response B is more appropriately concise than Response A. It strikes a better balance between providing sufficient detail and avoiding unnecessary wordiness or excessive brevity.

## Evaluation Steps
STEP 1: Analyze Response A based on the Verbosity criterion regarding completeness, conciseness, and overall balance.
STEP 2: Analyze Response B based on the Verbosity criterion regarding completeness, conciseness, and overall balance.
STEP 3: Compare the overall performance of Response A and Response B based on your analyses and assessment.
STEP 4: Output your preference of "A", "SAME" or "B" to the pairwise_choice field according to the Rating Rubric.
STEP 5: Output your assessment reasoning in the explanation field, justifying your choice by highlighting the specific strengths and weaknesses of each response in terms of verbosity.

# User Inputs and AI-generated Responses
## User Inputs
### Prompt
{prompt}

# AI-generated Responses

### Response A
{baseline_model_response}

### Response B
{response}
