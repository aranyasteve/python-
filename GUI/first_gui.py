from tkinter import *
from tkinter import messagebox
top = Tk()


def add():
    # a=input("Enter your name").capitalize()
    msg = messagebox.showinfo("Hello Python", "Hello sir")


C = Button(top, text="Salut!",  underline=4, justify=RIGHT,
           relief=RIDGE, bg='red', fg='white', activebackground='pink', activeforeground='yellow', font='Jokerman')

A = Button(top, text="Hi",  underline=4, justify=RIGHT,
           relief=RIDGE, bg='red', fg='white', activebackground='pink', activeforeground='yellow', font='Jokerman')
B = Button(top, text="Hello",  underline=4, justify=RIGHT,
           relief=RIDGE, bg='red', fg='white', activebackground='pink', activeforeground='yellow', font='Jokerman')
# B.place(x=10, y=10)
A.pack()
B.pack()
C.pack()
top.mainloop()


C = Canvas(top, bg="blue", height=250, width=300,cursor="mouse")

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill = "red")
line = C.create_line(10, 10, 240, 10, fill='white')
C.pack()
top.mainloop()




