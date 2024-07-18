from langchain_community.llms import GPT4All

llm = GPT4All(
    model="/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin"
)

llm.invoke("The first man on the moon was ... Let's think step by step")

# from gpt4all import GPT4All
# model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
# output = model.generate("The capital of France is ", max_tokens=3)
# print(output)