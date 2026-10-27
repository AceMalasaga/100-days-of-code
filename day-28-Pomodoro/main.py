import tkinter as tk
from tkinter import PhotoImage
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN =20
REPS = 0
TIMER = None
MARKS = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lbl.config(text="Timer")
    check_mark_lbl.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the timer"""
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If 8th
    if REPS % 8 == 0:
        #red
        count_down(long_break_sec)
        timer_lbl.config(text="Break", fg=RED, bg=YELLOW)
    # if it's 2nd, 4th, and 6th
    elif REPS % 2 == 0:
        #pink
        count_down(short_break_sec)
        timer_lbl.config(text="Break", fg=PINK, bg=YELLOW)
    # If it's 1st, 3rd, 5th, and 7th
    else:
        #work green
        count_down(work_sec)
        timer_lbl.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Count down the timer and display the count via format"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec =f"0{count_sec}"
    #change the canvas timer depending on the count
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #if count is greater than zero, execute the window.after
    if count > 0:
        global TIMER
        #Configuration: ms 1 seconds, called the count_down, and decrement the count to 1
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark_lbl.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
#Set the padding and bg color
window.config(padx=100, pady=50, bg=YELLOW)

#Set the width and Height and set the background color and thickness
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#Set Timer label and set the foreground color and font
timer_lbl = tk.Label(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
#Used the grid to set up what particular column and row
timer_lbl.grid(row=0, column=1)
#Extract the image using PhotoImage, since canvas can't directly use the image
tomato_img = PhotoImage(file="tomato.png")
#Set up the width and height and called the variable image
canvas.create_image(100, 112, image=tomato_img)
#Set the width and height of the canva text, fill, and font
#Set the canvas into a variable so it can be used letter
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
#place the canvas image to assigned column and row
canvas.grid(row=1, column=1)
#Button Start and Button reset
btn_start = tk.Button(text="Start", command=start_timer)
btn_start.grid(row=2, column=0)
btn_reset = tk.Button(text="Reset", command=reset_timer)
btn_reset.grid(row=2, column=2)
#check mark label
check_mark_lbl = tk.Label(font=(FONT_NAME, 18, "bold"),fg=GREEN, bg=YELLOW)
check_mark_lbl.grid(row=3, column=1)
window.mainloop()