from langchain.chat_models import init_chat_model
import os 
import pandas as pd 
import streamlit as st 
from dotenv import load_dotenv


load_dotenv()
llm  = init_chat_model(
    model ="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url =  "https://api.groq.com/openai/v1",
    api_key = os.getenv("api_key")
)

conversation = [
    {"role":"system","content":"You are a SQLite expert developer with 10 year of experience"}
]

csv_file = st.file_uploader("Enter path of CSV file : ")
df = pd.read_csv(csv_file)
st.write("CSV schema :")
st.write(df.dtypes)
   

while True:
    user_input=st.chat_input("Ask anything about the CSV file :",key="user")
    if user_input == "exit":
        break
    llm_input = f"""
        Table Name : data
        Table schema : {df.dtypes}
        Question : {user_input}
        Instruction :
            Write SQL query for the above question,
            Generate SQL query only in plain  text format and nothing else .
            If you cannot generate the query , then output 'Error'.
    """
    result = llm.invoke(llm_input)
    st.write(result.content)           