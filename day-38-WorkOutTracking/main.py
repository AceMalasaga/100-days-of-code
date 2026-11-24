import requests
import os
from datetime import datetime

API_KEY = os.environ.get("WORKOUT_API_KEY")
APP_ID = os.environ.get("WORKOUT_APP_ID")
USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_BEARER = os.environ.get("SHEETY_TOKEN")
SHEETY_HEADER = {
    "Authorization": f"Basic {SHEETY_BEARER}"
}
WORKOUT_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

PARAMS = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 49.5,
    "height_cm": 160,
    "age": 25,
}

API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = SHEETY_ENDPOINT

nutrition_response = requests.post(url=API_ENDPOINT, json=PARAMS, headers=WORKOUT_HEADERS)
nutrition_response.raise_for_status()

print(nutrition_response.json())
response_data = nutrition_response.json()['exercises']
today = datetime.today()
for exercise in response_data:
    sheety_body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=SHEETY_HEADER)
    print(sheety_response.text)