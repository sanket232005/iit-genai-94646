import streamlit as st 

if 'messages' not in st.session_state:
    st.session_state.message = []

with st.sidebar:
    st.header("Setting")
    choice = ["Upper", "Lower","Toggle"]
    mode = st.selectbox("select mode ",choice )
    count = st.slider("message count ",min_value=2 , max_value=10 ,value=6 , step=2)

    st.subheader("configure ")
    st.json({"mode":mode , "count":count})

st.title("Chatbot !!")
msg = st.chat_input("Say Something....")

if msg:
    outmsg = msg
    if mode=="Upper":
     outmsg = msg.upper()
    elif mode == "Lower":
     outmsg = msg.lower() 
    elif mode == "Toggle":
     outmsg = msg.swapcase()   
    st.session_state.message.append(msg)
    st.session_state.message.append(outmsg)

    msglist = st.session_state.message
    for idx, message in enumerate(msglist):
        role = "human" if idx % 2 == 0 else "ai"
        with st.chat_message(role):
            st.write(message)