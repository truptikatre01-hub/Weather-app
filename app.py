import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(
    page_title="Weather Application",
    page_icon="⛅"
)

st.title("⛅Weather App")
st.write("Enter your city name and click the button to get the weather")
city = st.text_input("Enter City Name")

API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

if st.button("Fetch Weather Data"):
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        st.success("Data fetch successfully")
        data = response.json()

        name = data["name"]
        country = data["sys"]["country"]
        st.subheader(f"Weather data for {name},{country}")
        # Fetch data in variables      
       


        temperature = data["main"]["temp"]
        humidity = data['main']['humidity']
        wind_speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🌡Temperature",f"🌡{temperature}°C")
        col2.metric("💧Humidity",f"💧{humidity}%")
        col3.metric("🍃Wind speed",f"🍃{wind_speed}m/s")
        col4.metric("☀️Weather Condition",f"☀️{weather}")

    else:
        st.error("Invalid city name")
        