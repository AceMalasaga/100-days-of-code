import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 7.448212 # Your latitude
MY_LONG = 125.809425 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def closer_position():
    latitude_max = MY_LAT + 5
    latitude_min = MY_LAT - 5
    longitude_max = MY_LONG + 5
    longitude_min = MY_LONG - 5
    return latitude_max, latitude_min, longitude_max, longitude_min

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/v2", params=parameters, timeout=10)
response.raise_for_status()
data = response.json()
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_time = time_now.hour
lat_max, lat_min, long_max, long_min = closer_position()

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if (lat_min <= iss_latitude <= lat_max) and (long_min <= iss_longitude <= long_max):
        if hour_time >= sunset or hour_time <= sunrise:
            my_email = input("Enter your email address: ").strip()
            password = input("Enter your password: ").strip()
            email = "acemalasaga252@gmail.com"
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:Reminders\n\nLookUp")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



