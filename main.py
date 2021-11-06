from tkinter import *
import pyperclip

def savePassword():
    with open("passwordManagerSaves.txt", 'a+') as file:
        file.write(f"{website} | {uname} | {passw}\n")
        print(website + uname + passw)
        entry_website.delete(0,'end')
        entry_password.delete(0,'end')
        destroyWind()


import random
import array
def genPass():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password = password + x

    entry_password.delete(0,'end')
    entry_password.insert(0,password)
    pyperclip.copy(password)


def destroyWind():
    top.destroy()


top = None
website = None,
uname = None,
passw = None
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)


def open_popup(website, uname, passw):
    global top
    top = Toplevel(window)
    top.geometry("340x65")
    top.config(padx=10, pady=10)
    top.title("Field Validation")
    if website == "" or passw == "" or uname == "":
        label = Label(top, text="Please Don't Leave Your Fields Empty!")
        label.grid(column=1, row=0)
        button = Button(top, text="Ok", width=14, command=destroyWind)
        button.grid(column=2, row=1)
    else:
        top.geometry("400x125")
        label1 = Label(top, text="Are You Sure?", font=("Arial", 10, "bold"))
        label1.grid(column=1, row=0)
        label = Label(top, text=f"Website: {website}\nUsername: {uname}\nPassword: {passw}")
        label.grid(column=2, row=1)
        button = Button(top, text="Save Password", width=14, command=savePassword)
        button.grid(column=3, row=2)


def check_fields():
    global website, uname, passw
    website = entry_website.get()
    uname = entry_email_uname.get()
    passw = entry_password.get()
    open_popup(website, uname, passw)


canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="lock.png").zoom(15).subsample(51)
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.insert(0, "hnsikora@gmail.com")
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password",command=genPass)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=check_fields)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
