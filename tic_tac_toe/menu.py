from tkinter import *
from tkinter import Tk, Button
from tic_tac_toe.functions import ply
from option import select


def players():
    top.destroy()
    ply()


def selectt():
    top.destroy()
    select()


top = Tk()
top.title("Tic Tac Toe")
top.minsize(450, 300)
top.resizable(height=False, width=False)
L = Label(text="Welcome to Tic Tac Toe Game!", font=("ariel", 20, "bold"))
L1 = Label(text="How Many Players ?", font=("ariel", 20, "bold"), justify=CENTER)
L.place(x=10, y=10)
L1.place(x=70, y=70)
B = Button(text="2 Players", font=("ariel", 15, "bold"), activebackground="white", command=players)
B1 = Button(text="1 Player", font=("ariel", 15, "bold"), activebackground="white", command=selectt)
B1.place(x=290, y=140)
B.place(x=30, y=140)
top.mainloop()

