import requests
from datetime import datetime

MY_LAT = 7.448212
MY_LONG = 125.809425

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get(url="https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)


