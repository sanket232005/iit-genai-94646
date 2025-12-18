import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("api_key")
url = "https://api.groq.com/openai/v1/chat/completions"
headers ={
    "Authorization" :f"Bearer {api_key}",
    "Content-Type" :"application/json"
}


req_data ={
        "model": "llama-3.3-70b-versatile",
        "messages":[
            {"role":"system","content":"you are experienced cricket commentator"},
            {"role":"user","content":"Who is god of cricket"},
            { "role": "assistant", "content": "Sachin Tendulkar." },
            { "role": "user", "content": "Where he born?" },    
        ],
    }

response = requests.post(url,json=req_data, headers =headers)
print("Status:",response.status_code)
resp=response.json()
print(resp["choices"][0]["message"]["content"])