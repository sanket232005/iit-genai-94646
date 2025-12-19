import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
url =  "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization" : f"Bearer {api_key}",
    "Content-Type" :"application/json"
}

user_prompt = input("Ask Anything :")

req_data = {
    "model" : "llama-3.3-70b-versatile",
    "messages" :[
        {"role":"user", "content":user_prompt}
    ],

}
time1= time.perf_counter()
response = requests.post(url,json=req_data,headers=headers)
time2= time.perf_counter()

resp=response.json()
print(resp["choices"][0]["message"]["content"])
print(f"Time Required :{time2-time1: .2f}sec")
