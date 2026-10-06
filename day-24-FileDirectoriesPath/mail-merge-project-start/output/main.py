#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with actual name
#Save the letters in the folder "ReadyToSave"

# name_list = []
# #['jennie\n', 'Eren\n', 'Luffy\n', 'Zoro\n', 'Sanji\n', 'Mikasa\n', 'Levi\n', 'Nami']
# #   0           1           2       3           4           5           6       7
#
# with open("../input/names/invited_names.txt", mode="r") as file:
#     #Use the readlines method to extract the names in the invited_names.txt
#     names = file.readlines()
#     for i in names:
#         #Append one by one
#         name_list.append(i)
#
# '''Dear [name],
#
# You're invited to my birthday this Saturday
#
# Hope you can make it
#
# Ace'''
# with open("../input/letters/starting_letter.txt", mode="r") as template:
#     #Get the template
#     template = template.read()
#
# for name in name_list:
#     #Remove the \n in name
#     clean_name = name.strip()
#     #replace the [name] in the template and change it to clean_name
#     change_name = template.replace("[name]", clean_name)
#     #Create a relative file path and insert the name of the file and name of the invited
#     file_path = f"./ReadyToSend/letter_for_{clean_name}.txt"
#     with open(file_path, mode="w") as inv_file:
#         #Create a file with all of that
#         inv_file.write(change_name)
PLACEHOLDER_NAME = "[name]"

with open("../input/names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("../input/letters/starting_letter.txt") as starting_letter:
    template = starting_letter.read()
    for name in names:
        cleaned_name = name.strip()
        letter_content = template.replace(PLACEHOLDER_NAME, cleaned_name)
        relative_path = f"./ReadyToSend/Letter_for_{cleaned_name}.txt"
        with open(relative_path, "w") as file:
            file.write(letter_content)