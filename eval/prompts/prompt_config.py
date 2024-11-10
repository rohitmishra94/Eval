from prompts import pointwise
from prompts import pairwise

pointwise_prompt_selector = {
    'fluency': pointwise.fluency,
    'coherence': pointwise.coherence,
    'groundedness': pointwise.groundedness,
    'instructions_following': pointwise.instructions_following,
    'multiturn_chat_quality': pointwise.multiturn_chat_quality,
    'multiturn_chat_safety': pointwise.multiturn_chat_safety,
    'question_answering_quality': pointwise.question_answering_quality,
    'summarization_quality': pointwise.summarization_quality,
    'safety': pointwise.safety,
    'text_quality': pointwise.text_quality,
    'verbosity': pointwise.verbosity,

}

pairwise_prompt_selector = {
    'multiturn_chat_quality': pairwise.multiturn_chat_quality,
    'multiturn_chat_safety': pairwise.multiturn_chat_safety,
    'question_answering_quality': pairwise.question_answering_quality,
    'summarization_quality': pairwise.summarization_quality,
    'safety': pairwise.safety,
    'text_quality': pairwise.text_quality,
    'verbosity': pairwise.verbosity,
    'fluency': pairwise.fluency,
    'coherence': pairwise.coherence,
    'groundedness': pairwise.groundedness,
    'instructions_following': pairwise.instructions_following,
}




