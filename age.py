import tkinter as tk
from tkinter import messagebox
from datetime import date

values=["January","February","March","April","May","June","July","August","September","October","November","December"]

def calculate_age():
    # Get the selected year, month, and day from the Spinboxes
    selected_year = int(year_spinbox.get())
    selected_month = month_spinbox.get()
    selected_day = int(day_spinbox.get())

    # Get the current date
    current_date = date.today()

    # Calculate the age
    age = current_date.year - selected_year - ((current_date.month, current_date.day) < (values.index(selected_month) + 1, selected_day))

    # Show the age in a message box
    messagebox.showinfo("Age", f"Your age is {age} years.")

window = tk.Tk()
window.config(bg="lightgrey")
window.geometry("600x400")
window.title("Age Calculator")
window.resizable(False,False)

tk.Label(window,text="AGE CALCULATOR",font=("Cambria",50),fg="blue",bg="lightgrey").pack(side="top")
tk.Label(window,text="Date Of Birth",font=("Ariel",30),fg="black",bg="lightgrey").pack(side="top")

tk.Label(window,text="Year",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
year_spinbox = tk.Spinbox(window,from_=1940, to=2024,state="readonly")
year_spinbox.pack(side="top")

tk.Label(window,text="Month",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
month_spinbox = tk.Spinbox(window, values=values, state="readonly")
month_spinbox.pack(side="top")

tk.Label(window,text="Day",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
day_spinbox = tk.Spinbox(window,from_=1, to=31,state="readonly")
day_spinbox.pack(side="top")

tk.Button(window,bd=10, bg="lightblue",width=10,text="Age",font=("Cambria",10), command=calculate_age).place(x=250,y=300)
def on_closing():
        if messagebox.askyesno(title="Quit", message="ARE YOU SURE YOU WANT TO QUIT?"):
            window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
