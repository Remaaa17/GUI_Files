from tkinter import *

top = Tk()
top.geometry("300x200")

cbtn1 = Checkbutton(top, text="red", fg="red")
cbtn1.pack()

cbtn2 = Checkbutton(top, text="Green", fg="green", activebackground="orange")
cbtn2.pack()

cbtn3 = Checkbutton(top, text="Blue", fg="blue", bg="yellow", width=10, height=3)
cbtn3.pack()

top.mainloop()
