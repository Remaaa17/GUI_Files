'''pack() Method'''
from tkinter import *

top = Tk()
top.geometry("300x200")

btn1 = Button(top, text="Login")
btn1.pack(side=LEFT)

top.mainloop()
#########################################################
'''Place() method'''
from tkinter import *

parent = Tk()
parent.title("Students")
parent.geometry("300x200")

name = Label(parent, text="Name : ")
name.place(x=50, y=50)
e1 = Entry(parent)
e1.place(x=100, y=50)

regno = Label(parent, text="Regd No : ")
regno.place(x=50, y=100)
e2 = Entry(parent)
e2.place(x=110, y=100)

parent.mainloop()
#######################################################
'''grid ()method'''
from tkinter import *

parent = Tk()
parent.title("Students")
parent.geometry("300x200")

name = Label(parent, text="Name : ")
name.grid(row=0, column=0, pady=10, padx=5)
e1 = Entry(parent)
e1.grid(row=0, column=1)

regno = Label(parent, text="Regd No : ")
regno.grid(row=1, column=0, pady=10, padx=5)
e2 = Entry(parent)
e2.grid(row=1, column=1)

btn = Button(parent, text="Submit")
btn.grid(row=3, column=1)

parent.mainloop()