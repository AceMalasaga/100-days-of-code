import requests
import os
from datetime import datetime

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXEL_USERNAME")
ID = os.environ.get("ID")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

GRAPH_CONFIG = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)

POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{ID}"

today = datetime.now()

POST_CONFIG = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.30"
}
# response = requests.post(url=POST_ENDPOINT, json=POST_CONFIG, headers=HEADERS)
# print(response.text)
past = datetime(2026, 11, 20)
yesterday = past.strftime("%Y%m%d")
UPDATE_ENDPOINT = f"{POST_ENDPOINT}/{yesterday}"

yesterday_update = {
    "quantity": "3.1"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=yesterday_update, headers=HEADERS)
# print(response.text)

response = requests.delete(url=UPDATE_ENDPOINT, headers=HEADERS)
print(response.text)