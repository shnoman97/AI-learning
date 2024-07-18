from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

model = Ollama(model="llama3")

# # PART 1: Create a ChatPromptTemplate using a template string
# print("-----Prompt from Template-----")
# template = "Tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic": "cats"})
# result = model.invoke(prompt)
# print(result)

# # PART 2: Prompt with Multiple Placeholders
# print("\n----- Prompt with Multiple Placeholders -----\n")
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} short story about a {animal}.
# Assistant:"""
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})

# result = model.invoke(prompt)
# print(result)

# PART 3: Prompt with System and Human Messages (Using Tuples)
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result)
