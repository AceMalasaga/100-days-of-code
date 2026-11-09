from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_list = {}

try:
    #If there is not yet words_to_learn
    french_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    #Use the original data
    original_data = pd.read_csv("data/french_words.csv")
    #Use the original_data in the data_list
    data_list = original_data.to_dict(orient="records")
else:
    #if the try success set the data_list to words_to_learn
    data_list = french_words.to_dict(orient="records")

# ---------------------------- NEXT RANDOM WORD SETUP ------------------------------- #
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(old_image, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(old_image, image=card_back_img)

# ---------------------------- SAVE PROGRESS SETUP ------------------------------ #
def is_known():
    data_list.remove(current_card)
    #My code
    # current_known.append(current_card)
    # current_known_french = pd.DataFrame(current_known, columns=["French", "English"])
    # current_known_french.to_csv("data/words_to_learn.csv", index=False)
    #Angela Code
    data = pd.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()
# ---------------------------- WINDOW SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# ---------------------------- CANVAS SETUP ------------------------------- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
old_image = canvas.create_image(400, 263, image=card_front_img)

# Text elements placed using coordinates from the layout guide
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Spans across 2 columns in a 2x2 grid
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS SETUP ------------------------------ #
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()