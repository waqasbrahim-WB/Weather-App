import streamlit as st
import requests
import os
from datetime import datetime

# -------------------------------
# Utility Functions
# -------------------------------

def load_groq_api_key():
    """Load Groq API key securely from environment variables."""
    return os.getenv("GROQ_API_KEY")

def fetch_weather_data(location="Karachi"):
    """
    Dummy weather data fetcher.
    Replace with actual API call (e.g., OpenWeatherMap).
    """
    return {
        "location": location,
        "temperature": 28,
        "real_feel": 30,
        "wind_speed": 12,
        "pressure": 1012,
        "humidity": 65,
        "sunrise": "06:45 AM",
        "sunset": "06:15 PM",
        "forecast": [
            {"day": "Mon", "temp": 28, "icon": "☀️"},
            {"day": "Tue", "temp": 27, "icon": "🌤️"},
            {"day": "Wed", "temp": 25, "icon": "🌧️"},
            {"day": "Thu", "temp": 26, "icon": "☁️"},
            {"day": "Fri", "temp": 29, "icon": "☀️"},
            {"day": "Sat", "temp": 30, "icon": "☀️"},
            {"day": "Sun", "temp": 31, "icon": "🌤️"},
        ],
        "rain_intervals": {
            "12AM": "10%",
            "3AM": "20%",
            "6AM": "40%",
            "9AM": "30%",
            "12PM": "15%",
            "3PM": "25%",
            "6PM": "35%",
            "9PM": "20%",
        }
    }

def groq_summary(weather_data):
    """
    Dummy Groq API integration.
    Replace with actual Groq API call using requests.
    """
    # Example: summarizing trend
    return "Expect warmer days ahead with occasional rain mid-week."

# -------------------------------
# Streamlit UI
# -------------------------------

# Page config
st.set_page_config(page_title="Weather Dashboard", layout="wide", initial_sidebar_state="expanded")

# Sidebar
st.sidebar.title("Weather Settings")
location = st.sidebar.text_input("Enter Location", "Karachi")
theme = st.sidebar.radio("Theme", ["Dark", "Light"])

# Apply theme (basic simulation)
if theme == "Dark":
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: #fafafa; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Fetch weather data
weather_data = fetch_weather_data(location)

# -------------------------------
# Layout
# -------------------------------

st.title("🌍 Sleek Weather Dashboard")

# Current Weather
st.subheader(f"Current Weather in {weather_data['location']}")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", f"{weather_data['temperature']} °C")
    st.metric("Real Feel", f"{weather_data['real_feel']} °C")
with col2:
    st.metric("Wind Speed", f"{weather_data['wind_speed']} km/h")
    st.metric("Pressure", f"{weather_data['pressure']} hPa")
with col3:
    st.metric("Humidity", f"{weather_data['humidity']} %")
    st.write(f"🌅 Sunrise: {weather_data['sunrise']}")
    st.write(f"🌇 Sunset: {weather_data['sunset']}")

# 7-Day Forecast
st.subheader("📅 7-Day Forecast")
forecast_cols = st.columns(len(weather_data["forecast"]))
for i, day in enumerate(weather_data["forecast"]):
    with forecast_cols[i]:
        st.write(day["day"])
        st.write(day["icon"])
        st.write(f"{day['temp']} °C")

# Rain Prediction Intervals
st.subheader("🌧️ Rain Prediction Intervals")
for time, chance in weather_data["rain_intervals"].items():
    st.write(f"{time}: {chance}")

# Global Weather Map
st.subheader("🌐 Global Weather Map")
if st.button("Explore Wind & Ocean Conditions"):
    st.info("Global weather map feature coming soon...")

# Other Cities
st.subheader("🏙️ Other Cities Overview")
cities = ["California", "Beijing", "Jerusalem"]
city_cols = st.columns(len(cities))
for i, city in enumerate(cities):
    city_data = fetch_weather_data(city)
    with city_cols[i]:
        st.write(f"**{city}**")
        st.write(f"🌡️ {city_data['temperature']} °C")
        st.write(f"💧 Humidity: {city_data['humidity']} %")

# Groq Summary
st.subheader("🤖 AI Weather Insights")
groq_api_key = load_groq_api_key()
if groq_api_key:
    summary = groq_summary(weather_data)
    st.success(summary)
else:
    st.warning("Groq API key not found. Please set GROQ_API_KEY in environment variables.")
