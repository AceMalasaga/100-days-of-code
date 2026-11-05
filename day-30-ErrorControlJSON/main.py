#FileNotFoundError
# try:
#     file = open("a_data.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_data.txt","w")
#     file.write("Something went wrong.")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File closed")
#     raise TypeError("This is an error I made up")


#KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]
# print(value)

#IndexError
# fruits = ["apple", "banana", "cherry"]
# fruit = fruits[3]

#TypeError
# text = "abc"
# print(text + 12)

# try:
#     pass
#     #Try something that might cause an exception
# except:
#     pass
#     #Do this if there was an exception
# else:
#     pass
#     #Do this if there were no exception
# finally:
#     pass
#     #Do this no matter what happened

# height = float(input("Enter your height in meters: "))
# weight = int(input("Enter your weight in kg: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / (height ** 2)
# print("Your BMI is: ", bmi)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError as error_message:
            print(f"That key {error_message} does not exist in the posts")

    return total_likes


count_likes(facebook_posts)
