from langchain_community.llms import Ollama

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# llm = Ollama(
#     model="llama3", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
# )
# res = llm.invoke("What is 81 divided by 9?")
# print("--------------------")
# print(res)

from langchain_core.messages import HumanMessage

llm = Ollama(model="llama3", format="json", temperature=0)

messages = [
    HumanMessage(
        content="What color is the sky at different times of the day? Respond using JSON"
    )
]

chat_model_response = llm.invoke(messages)
print(chat_model_response)