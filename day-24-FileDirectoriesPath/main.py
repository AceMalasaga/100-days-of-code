# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
#     file.close()

with open("../my_file.txt", mode="a") as file:
    content = input("Enter you content/s: ")
    file.write(content)

