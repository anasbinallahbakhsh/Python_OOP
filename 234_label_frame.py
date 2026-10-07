import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Label Frame')

label_frame = ttk.LabelFrame(win, text='Enter your details below')
label_frame.grid(row=0, column=0, )

labels = ['what is your name:?', 'what is your age:?', 'email', 'what is your gender?',
          'country:', 'state', 'City:', 'Address:']

for i in range(len(labels)):
    cur_label = ttk.Label(label_frame, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx=2, pady=2)

# entry boxes
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address': tk.StringVar()
}


counter = 0
for i in user_info:
    cur_entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter, padx=2, pady=2)
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
submit_btn.grid(row=2, columnspan=2)


for child in label_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)



win.mainloop()