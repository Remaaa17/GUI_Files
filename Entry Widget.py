from tkinter import *

top = Tk()
top.geometry("300x200")

enty0 = Entry(top, width="30")
enty0.place(x=50, y=40)

enty1 = Entry(top, bg="yellow")
enty1.place(x=50, y=70)

enty2 = Entry(top, fg="red", show="*")
enty2.place(x=50, y=100)

top.mainloop()
