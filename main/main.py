import tkinter 
from tkinter import messagebox
window = tkinter.Tk();
window.title("Login Form")
window.geometry('500x500' )
window.configure(bg='#FFFFFF')

def login():
    username = "abc"
    password = "123"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#FFFFFF')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#FFFFFF', fg="#000000", font=("Arial", 30,"bold"))
username_label = tkinter.Label(
    frame, text="Username :", bg='#FFFFFF', fg="#000000", font=("Arial", 16))
username_entry = tkinter.Entry(frame,bg='#FFFFFF',fg="black", font=("Arial", 16),insertbackground="black")
password_entry = tkinter.Entry(frame, show="*", bg='#FFFFFF',fg="black",font=("Arial", 16),insertbackground="black")
password_label = tkinter.Label(
    frame, text="Password :", bg='#FFFFFF', fg="#000000", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FFFFFF", fg="#000000", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()