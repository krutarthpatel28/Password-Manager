from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass_entry.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = web_entry.get()
    email_name = email_entry.get()
    pass_name = pass_entry.get()
    new_data = {
        website_name: {
            'email': email_name,
            'password': pass_name
        }
    }

    if len(website_name) == 0 or len(pass_name) == 0:
        messagebox.showinfo(title='LEFT ENTRIES EMPTY',
                            message='You have left a entry empty. Please fill all the entries to save password')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open('data.json')as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='NO DATA FILE FOUND')
    else:
        if website in data:
            email = data [website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title='Website not found', message='We dont have the data for the website you asked for')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

# website label
web_label = Label(text='Website:', font=("Courier", 10))
web_label.grid(row=2, column=1)
# website input
web_entry = Entry(width=36)
web_entry.focus()
web_entry.grid(row=2, column=2, columnspan=2)

# email or userid
email_lab = Label(text='E-mail/Username:', font=("Courier", 10))
email_lab.grid(row=3, column=1)
# email or id input
email_entry = Entry(width=36)
email_entry.insert(0, 'krutarthp704@gmail.com')
email_entry.grid(row=3, column=2, columnspan=2)

# password
password_lab = Label(text='Password:', font=("Courier", 10))
password_lab.grid(row=4, column=1)
# password input
pass_entry = Entry(width=36)
pass_entry.grid(row=4, column=2, columnspan=2)

# gen_pass_button
gen = Button(text='Generate Password', command=generate_pass)
gen.grid(row=4, column=4)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)

# search button
search = Button(text='Search', command=find_password)
search.grid(row=2, column=4, sticky='nesw')

window.mainloop()
