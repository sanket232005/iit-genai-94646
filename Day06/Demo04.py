from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

@tool
def calculator(expression):
    """
    this calcultaor function solves any arithmetic expression containing constatnt values . 
    it support basic arithmetic oerators +, -, * , / and parenthesis

    :param expression: str input arithmetic expression
    :return  expression result as str 

    """

    try: 
        result = eval(expression)
        return str(result)
    except:
        return "Error : Can Not solve Expression  "

@tool
def get_weather(city):
    """
    this get_weather function gets the currnt weather of given city .
    if weather can not be find return 'Error'
    this function does not return historical and general weather of the city.

    :param city :str input - city name 
    :return current weather in json format or 'Error'

    """
    print("called .....")
    try:
        api_key = os.getenv("api_key")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps (weather)
    except:
         return "Error" 

llm = init_chat_model(
    model = "google/gemma-3n-e4b:2",
    model_provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "dummy-key"
)

agent = create_agent(
    model = llm,
    tools=[calculator, get_weather],
    system_prompt="You are helpfull assistant . Answer in Short ."
)

while True:
    user_input = input("You ; ")
    if user_input == "exit":
        break
    result = agent.invoke({
        "messages": [
            {"role":"user","content":user_input}
        ]
    })
    llm_output = result["messages"][-1]
    print("AI : ",llm_output.content)
    # print("/n/n",result["message"])