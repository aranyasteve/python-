from tkinter import *
from tkinter import messagebox
top = Tk()


def click():
    messagebox.showinfo("file", "you have selected 1")


rb = Radiobutton(top, text="hello", bg="red", fg="blue", command=click, pady=10, padx=10, variable=IntVar, value=1,
                 state=ACTIVE, activebackground="blue", activeforeground="red")
rb2 = Radiobutton(top, text="hello", bg="red", fg="blue", command=click, pady=10, padx=10, variable=IntVar, value=2,
                  state=ACTIVE, activebackground="blue", activeforeground="red")
rb.place(x=10, y=10)
rb.place(x=0, y=70)
top.mainloop()
