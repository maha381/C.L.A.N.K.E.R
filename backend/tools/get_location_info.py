
from pathlib import Path



import requests
from datetime import datetime as dt, timedelta as td
import sqlite3
from urllib.parse import quote


from ..utils.tool_utils import timeDifferenceChecker

dbPath = Path(__file__).resolve().parents[2]/"data"/"cache"/"locationData.db"
dateFormat = "%Y-%m-%d %H:%M"

def setupDB():
    with sqlite3.connect(dbPath) as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS locations (
        place_name TEXT PRIMARY KEY,
        updated TEXT, 
        lat REAL, lng REAL, 
        timezone TEXT, 
        country TEXT, 
        county TEXT, 
        municipality TEXT, 
        elevation REAL, 
        population INTEGER, 
        feature_code TEXT
        )""")
        cursor.connection.commit()

setupDB()


def geocodingAPI(place: str) -> dict:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": quote(place), "count" : 1}

    try:
        response = requests.get(url, params=params)
        print(f"\033[92m{response.json()}\033[0m")
        data = response.json()["results"][0]
    except:
        raise ValueError(f"Could not fetch location data for {place}")

    #gets the name from the data instead of called name incase the api caught a mistake in the name or something

    new = {"place_name": data.get("name").lower(),
        "updated": dt.now().strftime(dateFormat),
        "coords": {
            "lat": data.get("latitude"),
            "lng": data.get("longitude")
        },
        "timezone": data.get("timezone"),
        "country": data.get("country"),
        "county": data.get("admin1"),
        "municipality": data.get("admin2"),
        "elevation": data.get("elevation"),
        "population": data.get("population"),
        "feature_code": data.get("feature_code")
    }
    return new


def get_location_info(place: str) -> dict:
    place = place.lower()

    with sqlite3.connect(dbPath) as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM locations WHERE place_name = ?", (place,))
            result = dict(cursor.fetchone())

            placeData = {
                "place_name": result["place_name"],
                "updated": result["updated"],
                "coords": {
                    "lat": result["lat"],
                    "lng": result["lng"]
                },
                "timezone": result["timezone"],
                "country": result["country"],
                "county": result["county"],
                "municipality": result["municipality"],
                "elevation": result["elevation"],
                "population": result["population"],
                "feature_code": result["feature_code"],

            }
        except:
            placeData = {}
        

        if placeData and timeDifferenceChecker(placeData["updated"], dt.now().strftime(dateFormat)) < td(days=365): #if data hasnt been updated in a year, get new instead
            return placeData
        try:
            new_entry = geocodingAPI(place)  
        except Exception as e:
            return f"Could not fetch location data for {place} | Error: {e}"
        cursor.execute("INSERT OR REPLACE INTO locations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        new_entry["place_name"], 
        new_entry["updated"], 
        new_entry["coords"]["lat"], 
        new_entry["coords"]["lng"],
        new_entry["timezone"],
        new_entry["country"], 
        new_entry["county"], 
        new_entry["municipality"],
        new_entry["elevation"],
        new_entry.get("population"),
        new_entry["feature_code"],
        ))
        connection.commit()

    return new_entry  
