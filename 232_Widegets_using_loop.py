#for loop
from re import subn
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("LOOP")

labels = ['what is your name:?', 'what is your age:?', 'email', 'what is your gender?',
          'country:', 'state', 'City:']


for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)


#entry box
name_var = tk.StringVar()

user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'email': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address':  tk.StringVar()
}

counter = 0

for i in user_info:
    cur_entrybox = 'entry' + i
    name_entrybox = ttk.Entry(
        win,
        width=16,
        textvariable=user_info[i]
    )
    name_entrybox.grid(column=1, row=counter)
    counter += 1


def submit():
    print("Name:", user_info['name'].get())
    print("Age:", user_info['age'].get())
    print("Email:", user_info['email'].get())
    print("Gender:", user_info['gender'].get())
    print("Country:", user_info['country'].get())
    print("State:", user_info['state'].get())
    print("City:", user_info['city'].get())
    print("Address:", user_info['address'].get())


submit_btn = ttk.Button(win, text='submit', command=submit)
submit_btn.grid(row=7, columnspan=2)


# name_entry = ttk.Entry(win, width=16, textvariable=user_info['name'])
# name_entry.grid(row=0, column=1)

win.mainloop()