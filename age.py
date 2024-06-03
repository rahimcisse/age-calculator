import tkinter as tk

values=["January","February","March","April","May","June","July","August","September","October","November","December"]


variable=tk.IntVar
def calculate():
    pass
window=tk.Tk()
window.config(bg="lightgrey")
window.geometry("600x400")
window.title("Age Calculator")
window.resizable(False,False)

tk.Label(window,text="AGE CALCULATOR",font=("Cambria",50),fg="blue",bg="lightgrey").pack(side="top")
tk.Label(window,text="Date Of Birth",font=("Ariel",30),fg="black",bg="lightgrey").pack(side="top")
tk.Label(window,text="Year",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
tk.Spinbox(window,from_=1980, to=2024,state="readonly").pack(side="top")

tk.Label(window,text="Month",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
j=tk.Spinbox(window,state="readonly",values=values).pack(side="top")
print()

tk.Label(window,text="Day",font=("Cambria",15),fg="black",bg="lightgrey").pack(side="top")
tk.Spinbox(window,from_=1, to=31,state="readonly").pack(side="top")
tk.Button(window,bd=10, bg="lightblue",width=10,text="Age",font=("Cambria",10), command=calculate).place(x=250,y=300)
window.mainloop()

window.mainloop()