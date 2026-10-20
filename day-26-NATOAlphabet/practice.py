import random
#List Comprehension
#Format: new_list = [new_item for item in list if test]

# numbers = [1, 2, 3]
# #List comprehension first expression (n + 1) followed by for loop
# new_list = [n+1 for n in numbers]
# print(new_list)

# names = ['Alex', "Beth", "Carolina", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]


#Dictionary Comprehension
#Format: new_dict = {new_key:new_value for item in list}
# students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

#Exercise 1

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # word_list = sentence.split()
# result = {word:len(word) for word in sentence.split()}


#Exercise 2

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:((temp_c * 9/5) + 32) for day, temp_c in weather_c.items()}
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "Ace", "Eren", "Luffy"],
    "score": [91, 84, 90, 87]
}

# for (key, value) in student_dict.items():
#     print(f"{key}: {value}")

#Looping through dictionary:
import pandas as pd

student_dt = pd.DataFrame(student_dict)
print(student_dt)

#Loop through a dataframe
# for (key, value) in student_dt.items():
#     print(value)

#Loop through rows of data frame
# for (index, row) in student_dt.iterrows():
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     if row.student == "Luffy":
#         print(row.score)

student_data = {index:row for (index, row) in student_dt.iterrows() if row.student == "Angela"}
print(student_data)