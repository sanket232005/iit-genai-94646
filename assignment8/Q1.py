from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import wrap_model_call
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(expression):
    """
    this calculator function solve the arithmetic expression containing constatnt values .
    it support basic arithmetic operators such as + , - , / ,* and parenthesis .

    :param expression : str input arithmetic expression
    :return expression result as str 

    """
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error : Can not solve expression "
    
@tool
def get_weather(city):
    """
    this get weather function get the current weather of given city . 
    if there is no information return the error.
    this function does not return historical and general weather of city.

    :param city: str input - city name 
    :return current weather in json format or error.

    """
    try:
        api_key = os.getenv("api_key")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url) 
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"
    
@tool
def read_file(filepath):
    """Read and return the contents of a text file."""

    with open(filepath,'r') as file:
        text = file.read()
        return text

@tool
def knowledge_lookup(topic: str) -> str:
    """Lookup basic knowledge about a topic."""
    
    knowledge_base = {
        "llm": "LLM (Large Language Model) is an AI model trained on large amounts of text to understand and generate human-like language.",
        "langchain": "LangChain is a framework for building applications using LLMs and tools.",
        "selenium": "Selenium is used to automate web browsers for testing.",
        "embeddings": "Embeddings are numerical representations of text used for similarity search."
    }

    return knowledge_base.get(topic.lower(), "No information available.")


@wrap_model_call
def model_logging(requests,handler):
    print(" Before Model Call ", "-" *20)
    response = handler(requests)
    print("After Model Call ")
    response.result[0].content=response.result[0].content.upper()
    return response

llm = init_chat_model(
    model ="google/gemma-3n-e4b:2",
    model_provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "dummy-key"
)

conversation = []

agent = create_agent(
    model = llm ,
    tools=[calculator,get_weather,read_file,knowledge_lookup],
    middleware=[model_logging],
    system_prompt="You are helpfull assistant . Answer in short ."
)

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    result = agent.invoke({
        "messages":[
            {"role":"user", "content":user_input}
        ]
    })
    llm_output = result["messages"][-1]
    print("AI : ",llm_output.content)