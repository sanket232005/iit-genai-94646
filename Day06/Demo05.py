from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call
import requests

@wrap_model_call
def model_logging(requests,handler):
    print("Before Model call ",'-' *20)
    response = handler(requests)
    print("After Model call ",'-' *20)
    response.result[0].content = response.result[0].content.upper()
    return response

@wrap_model_call
def limit_model_context(requests,handler):
    print(" * Before Model call ",'-' *20)
    response = handler(requests)
    print(" * After Model call ",'-' *20)
    response.result[0].content = response.result[0].content.upper()
    return response

llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "api_key"
)

conversation=[]

agent = create_agent(
    model = llm,
    tools=[],
    middleware=[model_logging,limit_model_context],
    system_prompt="You are Helpfull assistant . Answer in short ."
)

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    result = agent.invoke({
        "messages":[
            {"role":"user","content":user_input}
        ]
    })
    llm_output = result["messages"][-1]
    print("AI : ",llm_output.content)
