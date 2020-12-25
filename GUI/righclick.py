from tkinter import *


def cmd(event):
    print("Hello")
    b.config(text="c")


def cmd1():
    print("Hello")
    b.config(text="l")

top = Tk()
b = Button(text="h", command=cmd1)
b.bind('<Button-3>', cmd)
b.pack()
top.mainloop()
