import streamlit as st
import requests
from PIL import Image

# Function to get weather data
def get_weather(location, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data. Check the location."}

# Streamlit UI
st.set_page_config(page_title="Weather App", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.example.com/your-image.jpg'); /* Replace with your own URL */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with custom styling
st.title('🌞 Weather App 🌧️')

# Ask for the user's name and greet them
name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello **{name}**, welcome to the weather app! ')

# Ask for the location
location = st.text_input('Enter the location (city name):', '')

# If location is provided, fetch the weather
if location:
    api_key = "00d2ded3d50e718646d95f6d64930b70"  # Replace this with your actual key

    # Fetch weather data
    weather_data = get_weather(location, api_key)

    # Display weather data in Streamlit
    if 'error' in weather_data:
        st.error(weather_data['error'])
    else:
        if 'name' in weather_data and weather_data['name'].lower() != location.lower():
            st.write(
                f"The location '{location}' does not match the found city '{weather_data['name']}'. Please try again.")
        else:
            # Extract and display weather data
            city = weather_data['name']
            temperature = weather_data['main']['temp']
            weather_condition = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            icon = weather_data['weather'][0]['icon']

            # Display weather info
            st.write(f"### Weather in **{city}**:")
            st.image(f"http://openweathermap.org/img/wn/{icon}.png", width=100)
            st.write(f"**Temperature**: {temperature}°C")
            st.write(f"**Condition**: {weather_condition.capitalize()}")
            st.write(f"**Humidity**: {humidity}%")

            # Optional: Display a suggestion based on weather
            if 'rain' in weather_condition:
                st.write("Don't forget your umbrella! ☔")
            elif 'clear' in weather_condition:
                st.write("It's a sunny day! ☀️ Enjoy your day!")
            elif 'cloud' in weather_condition:
                st.write("Looks a bit cloudy today. ☁️")


# personal note cd "C:\Users\ala zbeda\Desktop\Project 1- weather\pythonProject61\weather app"
