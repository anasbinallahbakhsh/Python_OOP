#stater code 
import tkinter as tk
from tkinter import ttk 
win =tk.Tk()
win.title("MY first GUI")
#create a label 
name_label = ttk.Label(win, text='Enter your name ')
name_label.grid(row=0, column=0, )

email_label = ttk.Label(win, text='Enter your email')
email_label.grid(row=1, column=0, stick='W')


age_Label = ttk.Label(win, text='Eenter your age')
age_Label.grid(row=2, column=0, stick='W')

#create  enrty boc
name_entry_box  = ttk.Entry(win,width= 18) 
name_entry_box.grid(row=0 , column = 1)


win.mainloop()

