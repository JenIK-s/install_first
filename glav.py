from tkinter import *
from tkinter import ttk

def plus():
    global count
    count += 1
    coun['text'] = count


root = Tk()

root.title('First install')
root.geometry('100x50')

count = 0

coun = Label(root, text=count)
coun.pack()

button = ttk.Button(root, text='Click', command=plus)
button.pack()
root.mainloop()