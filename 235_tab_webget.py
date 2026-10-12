# note book contain two pages
#  page 1                          #page1
# widegets                          widgets

import tkinter as tk
from tkinter  import ttk
win=tk.Tk()
win.title('Tab control')
nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='page1')
nb.add(page2,text='page2')
# nb.grid(row=0,column=0)
nb.pack(expand=1,fill='both')

label1=tk.Label(page1,text='This is label')
label1.grid(row=0,column=0)

entry1=tk.Entry(page1,width=20)
entry1.grid(row=1,column=0)

label2=tk.Label(page2,text='This is label')
label2.grid(row=0,column=0)

win.mainloop()
