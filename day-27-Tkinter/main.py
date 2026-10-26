import tkinter as tk

#Button
def btn_clicked():
    app_label["text"] = input.get()

#Create a window using Tk method
window = tk.Tk()
#Title method change the title at the top of the window tkinter
window.title("My first GUI app")
#Set the minimum size to 500 and 400
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

#Label
#Configure the label
app_label = tk.Label(text="My first GUI app in Tkinter", font=("Arial", 12, "bold"))
#Call the pack method to display the app_label, by default the pack display at the top
# app_label.pack(side="left")
app_label.grid(row=0, column=0)

#Example to override the text in tk label
# app_label["text"] = "My first GUI app in Tkinter by Ace Malasaga"
# app_label.config(text="My first GUI app in Tkinter by Malasaga")

button1 = tk.Button(text="Click me", command=btn_clicked)
#In order to make anything appear on screen it needs to have some sort of layout(pack method)
button1.grid(row=1, column=1)

button2 = tk.Button(text="New button", command=btn_clicked)
button2.grid(row=0, column=2)

#Entry method use to put a text box
input = tk.Entry(width=20)
#Insert a text, works like a placeholder
input.insert(tk.END, "Some text to begin with")
#By using get method you can get the input
#pack is like packing all the widgets and display it in order layout
input.grid(row=2, column=3)

#Place which all about precise positioning
#Format .place(x=0, y=0) cons: too specific
#Grid
#Format .grid(column=0, row=0)
window.mainloop()