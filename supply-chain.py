from langchain_experimental.llms.ollama_functions import OllamaFunctions

model = OllamaFunctions(
    model="llama3", 
    format="json"
    )

def get_current_weather(location, unit):
    return 52

model = model.bind_tools(
    tools=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, " "e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location"],
            },
        }
    ],
    function_call={"name": "get_current_weather"},
)

response = model.invoke("what is the weather in ?")

print(response)