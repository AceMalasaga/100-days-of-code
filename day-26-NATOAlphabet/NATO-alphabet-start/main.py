# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
import pandas

nato_dt = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (_,row) in nato_dt.iterrows()}

while True:
    user_name = input("Enter your name: ").upper()
    if user_name == "EXIT":
        break
    else:
        nato_name = [nato_dict[letter] for letter in user_name if letter in nato_dict]
        print(nato_name)