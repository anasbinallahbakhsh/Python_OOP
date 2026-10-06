import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title("MY first GUI")

name_label = ttk.Label(win, text="Enter your name:")
name_label.grid(row=0, column=0)

email_label = ttk.Label(win, text="Enter your email")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="Enter your age")
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="Enter your gender")
gender_label.grid(row=3, column=0, sticky=tk.W)

name_var = tk.StringVar()
name_entry_box = ttk.Entry(win, width=16, textvariable=name_var)
name_entry_box.grid(row=0, column=1)

email_var = tk.StringVar()
email_entry_box = ttk.Entry(win, width=16, textvariable=email_var)
email_entry_box.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry_box = ttk.Entry(win, width=16, textvariable=age_var)
age_entry_box.grid(row=2, column=1)

gender_combobox = ttk.Combobox(win, width=16)
gender_combobox['values'] = ['Male', 'Female', 'Other']
gender_combobox.grid(row=3, column=1)

usertype_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype_var)
radiobtn1.grid(row=4, column=0)
radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype_var)
radiobtn2.grid(row=4, column=1)

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(
    win,
    text='Check if you want to subscribe to our newsletter',
    variable=checkbtn_var
)
checkbtn.grid(row=5, columnspan=3)


def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    user_gender = gender_combobox.get()
    user_type = usertype_var.get()

    if checkbtn_var.get() == 0:
        subscribed = "No"
    else:
        subscribed = "Yes"

    print(f"Hello {username}, your email is {useremail} and you are {userage} years old")
    print(user_gender, user_type)

    with open('anas.csv', 'a', newline='') as f:
        dict_writer_object = DictWriter(
            f, fieldnames=['Username', 'Email', 'Age', 'Gender', 'Type', 'Subscribed']
        )
        if f.tell() == 0:
            dict_writer_object.writeheader()
        dict_writer_object.writerow({
            'Username': username,
            'Email': useremail,
            'Age': userage,
            'Gender': user_gender,
            'Type': user_type,
            'Subscribed': subscribed
        })

    name_entry_box.delete(0, tk.END)
    email_entry_box.delete(0, tk.END)
    age_entry_box.delete(0, tk.END)


submit_button = ttk.Button(win, text="Submit", command=action)
submit_button.grid(row=6, column=0)

win.mainloop()