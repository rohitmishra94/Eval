def text_quality(prompt, baseline_model_response, response):
    return f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by two AI models. We will provide you with the user input and a pair of AI-generated responses (Response A and Response B). You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will first judge responses individually, following the Rating Rubric and Evaluation Steps. Then you will give step-by-step explanations for your judgment, compare the results, and declare the winner based on the Rating Rubric and Evaluation Steps.

# Evaluation
## Metric Definition
You will be assessing the Text Quality of each model's response, which measures how effectively the text conveys clear, accurate, and engaging information that directly addresses the user's prompt, considering factors like fluency, coherence, relevance, and conciseness.

## Criteria
Coherence: The response presents ideas in a logical and organized manner, with clear transitions and a consistent focus, making it easy to follow and understand.
Fluency: The text flows smoothly and naturally, adhering to grammatical rules and using appropriate vocabulary.
Instruction following: The response demonstrates a clear understanding of the task instructions, satisfying all of the instruction's requirements.
Groundedness: The response contains information included only in the context. The response does not reference any outside information.
Verbosity: The response is appropriately concise, providing sufficient detail without using complex language to thoroughly address the prompt without being overly wordy or excessively brief.

## Rating Rubric
"A": Response A demonstrates significantly better Text Quality than Response B as per criteria, excelling in aspects such as coherence, fluency, instruction following, groundedness, and verbosity.
"SAME": Response A and Response B demonstrate comparable Text Quality as per criteria, with no significant differences in aspects such as coherence, fluency, instruction following, groundedness, and verbosity.
"B": Response B demonstrates significantly better Text Quality than Response A as per criteria, excelling in aspects such as coherence, fluency, instruction following, groundedness, and verbosity.

## Evaluation Steps
STEP 1: Analyze Response A based on all the Criteria provided, including Coherence, Fluency, Instruction following, Groundedness, and Verbosity. Provide assessment according to each criterion.
STEP 2: Analyze Response B based on all the Criteria provided, including Coherence, Fluency, Instruction following, Groundedness, and Verbosity. Provide assessment according to each criterion.
STEP 3: Compare the overall performance of Response A and Response B based on your analyses and assessment of each criterion.
STEP 4: Output your preference of "A", "SAME" or "B" to the pairwise_choice field according to the Rating Rubric.
STEP 5: Output your assessment reasoning in the explanation field, justifying your choice by highlighting the specific strengths and weaknesses of each response in terms of Text Quality.

# User Inputs and AI-generated Responses
## User Inputs
### Prompt
{prompt}

# AI-generated Response

### Response A
{baseline_model_response}

### Response B
{response}
"""
