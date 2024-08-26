import os
#let us add a local llm_config
from llm_configs import *
import autogen
from autogen import ConversableAgent

"""
This first example shows how to create an agent and ask
a question.
"""

agent = ConversableAgent(
    name='chatbot',
    llm_config = deepseek_config,
    human_input_mode='NEVER'
)

reply = agent.generate_reply( 
    messages=[{
    'content':"Tell me a joke",
    'role':'user'}])

print(reply)
