from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FONT_STYLE = "Ubuntu"
BG_COLOR = "#000000"
FG_COLOR = "#EEEEEE"
TEXT_FILL = "#D84040"

# ---------------------------- SEACHBOX ------------------------------- #

def search_box():
    website_name = website_input.get().lower()
    
    try:
        with open("./data.json", "r") as saved_creds:
            saved_dict = json.load(saved_creds)
            saved_creds.close()
    except FileNotFoundError:
        messagebox.showinfo(title="Missing File", message="DataBase file missing.\nStart adding to create database file.")
    
    
    try:
        messagebox.showinfo(title=website_name.title(), message=f"Email:\n{saved_dict[website_name]["email"]}\n\n"
                                                        f"Password:\n{saved_dict[website_name]["password"]}")
    except KeyError:
        messagebox.showinfo(title=website_name, message=f"Could not find {website_name.title()}.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    
    password_input.delete(0, END)
    password_input.insert(index=END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_click():
    user_website = website_input.get().lower()
    user_email = username_input.get()
    user_password = password_input.get()

    cred_dict = {
        user_website:{
            "email":user_email,
            "password":user_password
        }
    }

    if (len(user_website)==0) or (len(user_password)==0):
        messagebox.showwarning(title="Oops!", message="Looks like a field is empty!")
    else:
        try:
            with open("./data.json", "r") as email_data:
                data = json.load(email_data)

        except FileNotFoundError:
            with open("./data.json", "w") as creation_file:
                json.dump(cred_dict, creation_file, indent=4)
                creation_file.close()
        else:
            data.update(cred_dict)
            email_data.close()

            with open("./data.json", "w") as email_data:
                json.dump(data, email_data, indent=4)
                email_data.close()
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

            username_input.insert(index=END, string="@gmail.com")
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

#-----/logo\-----#

canvas = Canvas(height=250, width=250, bg=BG_COLOR, highlightthickness=0)
lock_image = PhotoImage(file="./logo.png")
canvas.create_image(125,125,image=lock_image)
canvas.grid(column=1, row=0)

#-----/texts\-----#

website_text = Label(text="Website   ", bg=BG_COLOR, fg=TEXT_FILL, font=(FONT_STYLE, 15))
website_text.grid(column=0, row=1, sticky="w")

username_text = Label(text="Email   ", bg=BG_COLOR, fg=TEXT_FILL, font=(FONT_STYLE, 15))
username_text.grid(column=0, row=2, sticky="w")

password_text = Label(text="Password   ", bg=BG_COLOR, fg=TEXT_FILL, font=(FONT_STYLE, 15))
password_text.grid(column=0, row=3, sticky="w")


#-----/input boxes\-----#

website_input = Entry(width=31, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=(FONT_STYLE, 10, "bold"), insertbackground=FG_COLOR)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=50, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=(FONT_STYLE, 10, "bold"), insertbackground=FG_COLOR)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(index=END, string="@gmail.com")

password_input = Entry(width=31, bg=BG_COLOR, fg=FG_COLOR, highlightthickness=0, font=(FONT_STYLE, 10, "bold"), insertbackground=FG_COLOR)
password_input.grid(column=1, row=3)

#-----/buttons\-----#

generate_button = Button(text="Generate Password", bg=TEXT_FILL, fg=FG_COLOR, font=(FONT_STYLE, 10, "bold"), command=generate_password)
generate_button.grid(column=2, row=3)

submit_button = Button(text="Add", width=47, bg=TEXT_FILL, fg=FG_COLOR, font=(FONT_STYLE, 10, "bold"), command=add_click)
submit_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, bg=TEXT_FILL, fg=FG_COLOR, font=(FONT_STYLE, 10, "bold"), command=search_box)
search_button.grid(column=2, row=1)
window.mainloop()