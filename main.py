from random import shuffle, choices, randint
import tkinter as tk
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    """generates password when the user press the corresponding button"""
    entry_password.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_gen = (choices(letters, k=randint(8, 10)) + choices(symbols, k=randint(2, 4)) +
                    choices(numbers, k=randint(2, 4)))
    shuffle(password_gen)
    password_gen = "".join(password_gen)
    entry_password.insert(0, f"{password_gen}")
    pyperclip.copy(password_gen)


# ---------------------------- SEARCH ------------------------------- #
def find_website():
    """Search the data.json for stored info about the query made by the user"""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if entry_website.get() in data.keys():
            messagebox.showinfo(title=f"{entry_website.get()}",
                                message=f"Email: {data[entry_website.get()]['email']}\n"
                                        f"Password: {data[entry_website.get()]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {entry_website.get()} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    """saves the information given by the user into a .txt file"""
    data_dict = {
        entry_website.get(): {
            "email": entry_email.get(),
            "password": entry_password.get(),
        }
    }
    if len(entry_website.get()) < 1 or len(entry_email.get()) < 1 or len(entry_password.get()) < 1:
        messagebox.showwarning(title="Psst", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(data_dict)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_dict, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        entry_website.delete(0, "end")
        entry_password.delete(0, "end")
        entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# import pic
logo = tk.PhotoImage(file="logo.png")
# create a canvas
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# create label
website = tk.Label(text="Website:")
website.grid(row=1, column=0)
email_username = tk.Label(text="Email/Username:")
email_username.grid(row=2, column=0)
password = tk.Label(text="Password:")
password.grid(row=3, column=0)

# create entry
entry_website = tk.Entry(width=28)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_email = tk.Entry(width=48)
entry_email.grid(row=2, column=1, columnspan=2)
entry_password = tk.Entry(width=28)
entry_password.grid(row=3, column=1)

# create a button
button_search = tk.Button(text="Search", width=15, command=find_website)
button_search.grid(row=1, column=2)
button_add = tk.Button(text="Add", width=45, command=add)
button_add.grid(row=4, column=1, columnspan=2)
button_gen_pass = tk.Button(text="Generate Password", command=gen_pass)
button_gen_pass.grid(row=3, column=2)

window.mainloop()
