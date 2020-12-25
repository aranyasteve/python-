from tkinter import *
from Create1 import *
from Read1 import *


def create2():
    top.quit()
    Create().mainloop()

def read2():
    top.quit()
    Read().mainloop()

top = Tk()
top.title("Register or see you product information")
top.minsize(height=400, width=800)
top.resizable(height=False, width=False)
top.config(bg="#121b6e")
L = Label(top, text="Welcome, To register or check press the buttons below",
          bg="white", fg="#121b6e", font=("bold", 20))
L.place(x=80, y=5)
B = Button(top, text="Create", font=("bold", 15), bg="white", fg="#121b6e", activebackground="white",
           activeforeground="#121b6e", height=2, width=10, command=create2)
B.place(x=150, y=120)
B1 = Button(top, text="Read", font=("bold", 15), bg="white", fg="#121b6e", activebackground="white"
            , activeforeground="#121b6e", height=2, width=10, command=read2)
B1.place(x=530, y=120)
top.mainloop()