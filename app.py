import requests
import os
import json

from dotenv import find_dotenv, load_dotenv

# API Stuff
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")

# HTTPS Stuff
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# 1. Check Cache

# 2. Cache Response

# 3. Request Weather API
location = os.getenv("MY_LOCATION")
URL = f"{base_url}{location}?key={API_KEY}"
response = requests.get(URL)

# 4. Weather API Response
if response.status_code == 200:
    data = response.json()

    with open("weather_output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Weather data saved to weather_output.json")
else:
    print(response.text)

# 5. Save Cached Results