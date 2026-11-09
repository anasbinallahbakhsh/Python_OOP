import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()

# label frame
label_frame = ttk.LabelFrame(win, text='Contact Detail')
label_frame.grid(row=0, column=0, padx=40, pady=10)

# labels
name_label = ttk.Label(label_frame, text='Enter your Name please : ')
age_label = ttk.Label(label_frame, text='Enter your age please : ')

# entry box variables
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes
name_entry = ttk.Entry(label_frame, width=36, textvariable=name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable=age_var)

# grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)


def submit():
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error', 'Please fill both name and age')
    else:
        try:
            age = int(age)
            m_box.showinfo('Success', f'Name: {name}, Age: {age}')
        except ValueError:
            m_box.showerror('Error', 'Age must be a number')
        else:
            if age < 18:
                m_box.showwarning('waring','you are not of 18 so u canot  opeen this gui')
                print(f'{name} : {age}')
submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1, column=0, columnspan=2, pady=10)

win.mainloop()