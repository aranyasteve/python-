from tkinter import *
from tic_tac_toe.functions import hard, easy


def select():
    top = Tk()

    def easyy():
        top.destroy()
        easy()

    def hardd():
        top.destroy()
        hard()

    top.title("Tic Tac Toe ")
    l2 = Label(top, text="Select a Difficulty", font=("ariel", 20, "bold"))
    l2.place(x=10, y=10)
    b = Button(top, text="Normal", font=("ariel", 15, "bold"), activebackground="white", command=easyy)
    b1 = Button(top, text="Impossible", font=("ariel", 15, "bold"), activebackground="white", command=hardd)
    b1.place(x=100, y=70)
    b.place(x=10, y=70)
    top.minsize(250, 200)
    top.resizable(height=False, width=False)
    top.mainloop()



