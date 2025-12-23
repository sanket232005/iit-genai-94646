from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv

# llm = init_chat_model(
#     model="google/gemma-3n-e4b",
#     api_key = "dummey_key",
#     model_provider="openai",
#     base_url = "http://127.0.0.1:1234/v1"
# )

load_dotenv()

llm = init_chat_model(
    model ="llama-3.3-70b-versatile",
    model_provider="openai",
    api_key = os.getenv("api_key"),
    base_url = "https://api.groq.com/openai/v1"
)

conversation = list()
while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    user_msg = {"role":"user","content":user_input}
    conversation.append(user_msg)
    llm_output = llm.invoke(conversation)
    print("AI :",llm_output.content)
    llm_msg = {"role":"assistant","content":llm_output.content}
    conversation.append(llm_msg)