from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def calculator(expression):
    """
    this calculator function solves any arithmetic expression containing all constatnt values,
    it support basic arithmetic operators +, -, *, /, and parenthesis,

    :param expression : str input arithmetic expression 
    :returns expression result as str 
    """
    print("called .....")
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error : Cannot solve expression "
    
llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "dummy-key"

)

agent = create_agent(
    model = llm,
    tools=[calculator],
    system_prompt="Yor are helpfull assistant . Answer in shot"
)

while True:
    user_input = input ("You : ")
    if user_input == "exit":
        break
    result = agent.invoke({
        "messages": [
            {"role":"user","content":user_input}
        ]
    })
    llm_output = result["messages"][-1]
    print("AI :",llm_output.content)
    