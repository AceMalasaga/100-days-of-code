from random import randint
from tkinter import *
from tkinter import messagebox as mbox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '(', ')']

    #Use list comprehension to shorten it and add a range on how many letters, numbers, or symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    #use + to flat the list and don't use [letters,num]
    password_list = password_letters + password_numbers + password_symbols
    #shuffle the password_list
    shuffle(password_list)

    #use the join method to combine the password_list into a single string instead of list
    password = "".join(password_list)
    #Insert the generated password in the entry password
    password_entry.insert(0, password)
    #Install and use pyperclip library and use it
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if not website.strip() or not email.strip() or not password.strip():
        mbox.showerror(title="Error", message="Please enter all required information")
        return
    else:
        is_okay = mbox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \n is it okay to save?")

        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

#Label
web_lbl = Label(text="Website:")
web_lbl.grid(row=1, column=0)

user_name_lbl = Label(text="Email/Username:")
user_name_lbl.grid(row=2, column=0)

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
web_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
username_entry.insert(0, "@cer@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#Buttons
gen_pass_btn = Button(text="Generate Password", width=14, command=generate_password)
gen_pass_btn.grid(row=3, column=2, sticky="ew")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew")


window.mainloop()
