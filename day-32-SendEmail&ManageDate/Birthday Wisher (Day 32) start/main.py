# import smtplib
#
# my_email = input("Enter your email: ").strip()
# password = input("Enter your app password: ").strip()
# send_to = input("Enter recipient email address: ").strip()
# subject = input("Enter your subject: ").strip()
# body = input("Enter your body: ").strip()
# message = f"Subject:{subject}\n\n{body}".title().strip()
#
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs=send_to,
#                         msg=message)

# import datetime as dt
#
# now = dt.datetime.now()
# year =now.year
#
# day_of_week = now.weekday()
# print(year, day_of_week)
#
# date_of_birth = dt.datetime(year=2001, month=9, day=30, hour=9)
# print(date_of_birth)
# from random import choice
# with open("quotes.txt") as quotes:
#     content = quotes.read().splitlines()
# print(content[choice(range(1, len(content)))])

import datetime as dt
import smtplib
from random import choice

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quotes = choice(all_quotes)

    my_email = input("Enter your email address: ").strip()
    password = input("Enter your password: ").strip()
    send_to = input("Enter recipient email address: ").strip()
    body = quotes
    message = f"Subject:Tuesday Quotes\n\n{body}".title().strip()

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=send_to,msg=message)