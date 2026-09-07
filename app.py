import streamlit as st
import requests

st.title("🌦️ Weather App")

city = st.text_input("Enter a city:")

if city:
    # Search for the city
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if "results" in geo_data:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        city_name = geo_data["results"][0]["name"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        temperature = weather_data["current"]["temperature_2m"]
        humidity = weather_data["current"]["relative_humidity_2m"]
        wind = weather_data["current"]["wind_speed_10m"]

        st.subheader(f"📍 {city_name}")

        st.write(f"🌡️ Temperature: {temperature} °C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"💨 Wind speed: {wind} km/h")

    else:
        st.error("City not found.")
