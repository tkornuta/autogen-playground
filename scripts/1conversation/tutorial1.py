import os

from autogen import ConversableAgent

agent = ConversableAgent(
    "chatbot",
    llm_config={
        "config_list": [
            {"model": "gpt-3.5-turbo",
             "api_key": os.environ.get("OPENAI_API_KEY"),
             "temperature": 1.0,
             "cache_seed": None # Disable caching
            }
        ]
    },
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)
