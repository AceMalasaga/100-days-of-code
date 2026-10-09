# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temp_list = []
#     for row in data[1:]:
#         print(row)
#         temp_list.append(int(row[1]))
#     print(temp_list)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#
#     for row in data:
#         if row[1] != "temp":
#             temp_list.append(int(row[1]))
#     print(temp_list)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())
# print(data["temp"].max())

#Get data in column
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])

#Print the row of data which had the highest temperature
# print(data[data.temp == max(data.temp)])

#Convert Monday's Temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# fahrenheit  = (monday.temp[0] * 9/5) + 32
# print(fahrenheit )

#Create a dataframe from scratch
data_dict = {
    "student": ["Ace", "Jennie", "Angela"],
    "score": [80, 79, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
