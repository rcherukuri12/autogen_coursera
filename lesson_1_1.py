from pprint import pprint
import os
#let us add a local llm_config
from llm_configs import *
import autogen
from autogen import ConversableAgent

"""
This second example shows how to create two agents and making jokes.
Both are using different LLMs
"""

cathy = ConversableAgent(
    name='cathy',
    system_message="Your name is Cathy and you are a stand-up comedian.",
    llm_config = deepseek_config,
    human_input_mode='NEVER'
)
joe = ConversableAgent(
    name='joe',
    system_message="Your name is Joe and you are a stand-up comedian. \
    Start the next joke from the punchline of the previous joke.",
    llm_config = phi3_config,
    human_input_mode='NEVER'
)
chat_result = joe.initiate_chat(recipient=cathy, 
                                message ="I am Joe. Cathy, let's keep the jokes rolling.",
                                max_turns=3)
pprint(chat_result.cost)



