import os
import pprint

from autogen import ConversableAgent

llm_config={
    "config_list": [
        {"model": "gpt-3.5-turbo", "api_key": os.environ.get("OPENAI_API_KEY")}
    ]
}


cathy = ConversableAgent(
    name="cathy",
    system_message=
    "Your name is Cathy and you are a stand-up comedian.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="joe",
    system_message=
    "Your name is Joe and you are a stand-up comedian. "
    "Start the next joke from the punchline of the previous joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

chat_result = joe.initiate_chat(
    recipient=cathy, 
    message="I'm Joe. Cathy, let's keep the jokes rolling.",
    max_turns=2,
)

pprint.pprint(chat_result.chat_history)
pprint.pprint(chat_result.cost)
pprint.pprint(chat_result.summary)
