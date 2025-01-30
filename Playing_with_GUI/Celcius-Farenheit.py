import tkinter as tk
from tkinter import *
a = "F"
b = "C"
window = tk.Tk()
window.title("Celsius to Fahrenheit calculator")
window.configure(background="cyan")



label2 = Label(text="Type the ",font="Georgia 27",height=1,)
label2.grid(column=1,row=0)

label2 = Label(text="Temperature",font="Georgia 27",height=1,)
label2.grid(column=2,row=0)

label2 = Label(text=" in celsius",font="Georgia 27",height=1,)
label2.grid(column=3,row=0)

entry = Entry(width=20)
#Add some text to begin with
entry.insert(END, string=b)
entry.grid(column=1,row=2)

def action1():
    global a
    a = str(entry.get())
    print(a)
    entry1.delete(0,END)
    entry1.insert(END,str((float(a)*9/5)+32))

button = Button(text="->", command=action1)
button.grid(column=2, row=2)

def action():
    global b
    b = str(entry.get())
    print(b)
    entry.delete(0,END)
    entry.insert(END,str((float(b)-32)*5/9))

button1 = Button(text="<-", command=action)
button1.grid(column=2, row=3)

entry1 = Entry(width=20)
#Add some text to begin with
entry1.insert(END, string=a)
entry1.grid(column=3,row=2)

window.minsize(500,600)
window.mainloop()

