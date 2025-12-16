import streamlit as st
import requests
import os
from dotenv import load_dotenv

def weather():
    city = st.text_input("Enter City Name ")

    load_dotenv()
    api_key = os.getenv("api_key")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response= requests.get(url)
    weather = response.json()

    if response.status_code==200:
        st.write("Temperature :",weather['main']['temp'])
        st.write("Humidity :",weather['main']['humidity'])
        st.write("Wind Speed :",weather['wind']['speed'])
    else:
        st.error(weather.get("message","Error fetching weather ")) 
       

if "login" not in st.session_state:
    st.session_state.login = False

st.title ("Login Form !!")

if not  st.session_state.login:
    user= st.text_input("Enter Username..")
    password = st.text_input("Enter Password ..", type ="password")


    if st.button("Log in", type = "primary"):
      if user == password and user != "":
         st.session_state.login = True
         st.success("You Are Logged In !!")
      else:
         st.error("Invalid Username and Password ")
else:
     st.title("Welcome To Weather App ")
     weather()  

    
  