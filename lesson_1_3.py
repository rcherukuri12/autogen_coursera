from pprint import pprint
import os
#let us add a local llm_config
from llm_configs import *
import autogen
from autogen import ConversableAgent

"""
This fourth example shows how to create two agents and making jokes.
They simply keep talking until one says : I gotta go
Both are using different LLMs
Finally we ask the LLMs to summarize

"""

cathy = ConversableAgent(
    name='cathy',
    system_message="Your name is Cathy and you are a stand-up comedian.\
        When you're ready to end conversation, say 'I gotta go'.",
    llm_config = deepseek_config,
    human_input_mode='NEVER',
    is_termination_msg= lambda msg:"I gotta go" in msg["content"]
)
joe = ConversableAgent(
    name='joe',
    system_message="Your name is Joe and you are a stand-up comedian. \
    Start the next joke from the punchline of the previous joke.\
        When you're ready to end conversation, say 'I gotta go'.",
    llm_config = phi3_config,
    human_input_mode='NEVER',
    is_termination_msg= lambda msg:"I gotta go" in msg["content"]
)
chat_result = joe.initiate_chat(recipient=cathy, 
                                message ="I am Joe. Cathy, let's keep the jokes rolling.",
                                # adding the following two would now get whole summary
                                summary_method="reflection_with_llm",
                                summary_prompt="Summarize the conversation")
pprint(chat_result.cost)
pprint(chat_result.summary)



