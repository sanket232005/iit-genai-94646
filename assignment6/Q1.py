import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ---------------- ONLINE MODEL (LOCAL - LM STUDIO) ----------------
def offline_model(user_prompt):
    url = "http://127.0.0.1:1234/v1/chat/completions"

    headers = {
        "Authorization": "Bearer dummy_key",
        "Content-Type": "application/json"
    }

    req_data = {
        "model": "google/gemma-3-4b",
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post(url, json=req_data, headers=headers)
    resp = response.json()

    if "choices" in resp:
        return resp["choices"][0]["message"]["content"]
    else:
        return f"Local Model Error: {resp}"


# ---------------- OFFLINE MODEL (GROQ CLOUD) ----------------
def online_model(user_prompt):
    api_key = os.getenv("api_key")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    req_data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post(url, json=req_data, headers=headers)
    resp = response.json()

    if "choices" in resp:
        return resp["choices"][0]["message"]["content"]
    else:
        return f"Groq API Error: {resp}"


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 Choose Model")
    mode = st.selectbox("Select Model", ["Online", "Offline"])

    st.divider()
    st.subheader("🕘 History")

    if st.session_state.messages:
        for role, msg in st.session_state.messages:
            st.write(f"**{role.capitalize()}**: {msg}")
    else:
        st.write("No chat history yet.")

    if st.button("🗑 Clear History"):
        st.session_state.messages = []
        st.rerun()

# ---------------- CHAT UI ----------------
st.title("Sunbeam ChatGPT")

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

user_prompt = st.chat_input("Ask Anything...")

if user_prompt:
    # store user message
    st.session_state.messages.append(("user", user_prompt))
    with st.chat_message("user"):
        st.write(user_prompt)

    # model selection
    if mode == "Online":
        reply = online_model(user_prompt)
    else:
        reply = offline_model(user_prompt)

    # store assistant message
    st.session_state.messages.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)
