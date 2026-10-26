#So basically unlimited positional argument in tuple format
# def add(*args):
#     print(type(args))
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(10, 20, 30, 40, 50))

#So basically many keyword arguments, hence called kwargs (keyword argument) in a dict format
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multi"]
#     print(n)
#
#
# num1 = int(input("Enter the first number: "))
# calculate(num1, add=8, multi=4)

# class Car:
#
#     def __init__(self, **kwargs):
#         #get function similar way to use it as square bracket, but the benefit of get is that if the model key doesn't exit in the dictionary
#         #then it will just return none it won't give an error
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#
# my_car = Car(make="Ford")
# print(my_car.make)
import tkinter as tk

#Create a window using Tk method
window = tk.Tk()
#Title method change the title at the top of the window tkinter
window.title("My first GUI app")
#Set the minimum size to 500 and 400
window.minsize(width=500, height=400)

#Label
#Configure the label
app_label = tk.Label(text="My first GUI app in Tkinter", font=("Arial", 12, "bold"))
#Call the pack method to display the app_label, by default the pack display at the top
# app_label.pack(side="left")
app_label.pack()

#Example to override the text in tk label
# app_label["text"] = "My first GUI app in Tkinter by Ace Malasaga"
# app_label.config(text="My first GUI app in Tkinter by Malasaga")

#Button
def btn_clicked():
    app_label["text"] = input.get()

button = tk.Button(text="Click me", command=btn_clicked)
#In order to make anything appear on screen it needs to have some sort of layout(pack method)
button.pack()

#Entry
#Entry method use to put a text box
input = tk.Entry(width=20)
#Insert a text, works like a placeholder
input.insert(tk.END, "Some text to begin with")
input.pack()
#By using get method you can get the input
# input.get()

#Text
text = tk.Text(width=20, height=5)
#Put the cursor directly in the textbox
text.focus()
#Get current value in textbox at line 1, character 0
text.insert(tk.END, "Example of Multi-line text entry")
print(text.get("1.0", tk.END))
text.pack()

#Spinbox
def spinbox_used():
    #Gets the current value in spinbox.
    print(spinbox.get())

spinbox = tk.Spinbox(width=5, from_=0, to=10, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
#scale from 0 to 100, called the scale function to print the value
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbtn_used():
    #print 1 if on button is checked, otherwise 0
    print(checked_state.get())
checked_state = tk.IntVar()
checkbtn = tk.Checkbutton(text="Is On", variable=checked_state, command=checkbtn_used)
checked_state.get()
checkbtn.pack()

#Radio Button
def radio_used():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobtn1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobtn2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobtn1.pack()
radiobtn2.pack()

#ListBox
def listbox_used(event):
    #get the current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Orange", "Banana", "Cherry"]

for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()