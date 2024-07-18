from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize the callback manager with a streaming stdout handler
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Initialize the Ollama model with Llama-3
llm = Ollama(model="llama3", callback_manager=callback_manager)

# Define a prompt template
template = """
You are a helpful assistant. Answer the following question.

Question: {question}

Answer:
"""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Set up the LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Sample question
question = "The first man on the moon was ..."

# Run the LLM chain
response = chain.invoke(question)

# Print the response
print(response)
