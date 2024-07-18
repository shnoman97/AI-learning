from langchain_community.llms import Ollama

model = Ollama(model="llama3")


# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print(result)
