import streamlit as st 
from  langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
st.title("Chatbot !!")

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    api_key = os.getenv("api_key"),
    model_provider= "openai",
    base_url = "https://api.groq.com/openai/v1"
)

user_input = st.chat_input("Ask Anything ....")
if user_input:
#     result = llm.stream(user_input)
#     for chunk in result:
#         st.write(chunk.content)
    result = llm.invoke(user_input)
    st.write(result.content)       

