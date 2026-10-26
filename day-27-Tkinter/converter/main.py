import tkinter as tk

def miles_to_kilometers():
    km = float(miles.get()) * 1.609344
    result_lbl.config(text=f"{km:.2f}")


window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#Entry
miles = tk.Entry(width=10)
miles.grid(row=0, column=1)

#Label
miles_lbl = tk.Label(text="Miles", font=("Arial", 8))
miles_lbl.grid(row=0, column=2)

equal_lbl = tk.Label(text="is equal to", font=("Arial", 8))
equal_lbl.grid(row=1, column=0)

result_lbl = tk.Label(text="0", font=("Arial", 8))
result_lbl.grid(row=1, column=1)

km_lbl = tk.Label(text="Km", font=("Arial", 8))
km_lbl.grid(row=1, column=2)

#Button
button1 = tk.Button(text="Calculate", command=miles_to_kilometers)
button1.grid(row=2, column=1)



window.mainloop()