import requests
import smtplib
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "lat": 33.220211,
    "lon": 132.563797,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=f"{OWM_ENDPOINT}", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]

will_rain = False
for hour_data in weather_list:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("PASSWORD")
    to_email = os.environ.get("TO_EMAIL")
    body = "It's going to rain today. Remember to bring an Umbrella!"
    with smtplib.SMTP('smtp.gmail.com')as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Weather Update\n\n{body}")