import requests
import json
from .get_location_info import get_location_info
#use try instead of if to check if place in cache, more efficent as doesnt have to look through, if works work, if not get new (api)


def get_weather(place: dict) -> dict: 

    coords = get_location_info(place)["coords"]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
            "latitude":  coords["lat"],
            "longitude": coords["lng"],
            "current": ["weather_code", "cloud_cover", "precipitation", "rain", "snowfall", "wind_speed_10m", "temperature_2m", "relative_humidity_2m", "apparent_temperature"],
            "temperature_unit" : "celsius"
            }
    try:
        response = requests.get(url, params).json()
    except Exception as e:
        return f"could not fetch weather data for {place} | Error: {e}"

    return {place: response["current"]}


