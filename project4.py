#Written by Shiven Desai
import tkinter as tk
from tkinter import messagebox

# create a Tkinter window
window = tk.Tk()
window.title("Calculate Total")

# create a label widget
lbl = tk.Label(window, text="Click the button to calculate the total")
lbl.pack()

# function to calculate the total
def calculate_total():
    try:
        # open the file for reading
        with open("numbers.txt", "r") as file:
            total = 0
            for line in file:
                # convert each line to an integer and add to total
                num = int(line.strip())
                total += num
            # display the total in a message box
            messagebox.showinfo("Total", "The total is " + str(total))
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

# create a button widget
btn = tk.Button(window, text="Calculate", command=calculate_total)
btn.pack()

# run the main event loop
window.mainloop()
