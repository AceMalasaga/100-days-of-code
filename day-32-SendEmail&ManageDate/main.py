import pandas as pd
import datetime as dt
from random import choice
import smtplib
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
birth_data = pd.read_csv("birthdays.csv")
birth_list = birth_data.to_dict(orient="records")

#date
now = dt.datetime.now()
birth_month = now.month
birth_day = now.day
birth_date = (birth_month, birth_day)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

birthdays_dict = {(i['month'], i['day']): i for i in birth_list}

#HINT 3: Then you could compare and see if today's month/day matches
# one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if birth_date in birthdays_dict:
    name = birthdays_dict[birth_date]["name"]
    email = birthdays_dict[birth_date]["email"]
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    rand_letter = choice(letters)
    with open(f"letter_templates/{rand_letter}", "r") as file:
        content = file.read()
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
        # with the person's actual name from birthdays.csv
        # HINT: https://www.w3schools.com/python/ref_string_replace.asp
        greetings = content.replace("[NAME]", name)

    my_email = input("Enter your email address: ").strip()
    password = input("Enter your password: ").strip()

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com),
    # Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday {name}\n\n{greetings}")



