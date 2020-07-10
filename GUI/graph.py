from tkinter import *
from tkinter import messagebox

top = Tk()


def canvas():
    c = Canvas(top, bg="red", height=250, width=300, cursor="mouse")
    coord = 10, 50, 240, 210
    c.create_arc(coord, start=0, extent=150, fill="blue")
    # c.create_line(coord, fill="blue")
    c.pack()


def canvas1():
    c1 = Canvas(top, bg="yellow", height=250, width=300, cursor="mouse")
    coord = 10, 50, 240, 210
    c1.create_line(coord, fill="pink")
    c1.pack()


def canvas2():
    c2 = Canvas(top, bg="maroon", height=250, width=300, cursor="mouse")
    coord = 100, 50, 240, 210
    c2.create_rectangle(coord, fill="violet")
    # c2.create_line(10, 10, 100, 100, fill="violet")
    c2.pack()


def canvas3():
    c3 = Canvas(top, bg="green", height=250, width=300, cursor="mouse")
    coord = 100, 250, 250, 100
    c3.create_oval(coord, fill='light blue')
    c3.pack()


def canvas4():
    c4 = Canvas(top, bg="dark red", height=250, width=300, cursor="mouse")
    coord = 0, 25, 200, 100, 0, 225
    c4.create_polygon(coord, fill="light blue")
    c4.pack()


def click():
    messagebox.showinfo("file", "You have got an Arc! {}".format(canvas()))


def click1():
    messagebox.showinfo("file", "You have got a line! {}".format(canvas1()))


def click2():
    messagebox.showinfo("file", "You have got a Rectangle! {}".format(canvas2()))


def click3():
    messagebox.showinfo("file", "You have got a Circle! {}".format(canvas3()))


def click4():
    messagebox.showinfo("file", "You have got a Polygon! {}".format(canvas4()))


Button4 = Button(top, command=click4, text="Polygon", relief=GROOVE, bg="light blue", fg="green",
                 activebackground="green", activeforeground="light blue", justify=LEFT, pady=10, padx=10, state=ACTIVE)
Button3 = Button(top, text="Circle", command=click3, relief=GROOVE, bg="light blue", fg="dark red",
                 activebackground="dark red", activeforeground="light blue", justify=LEFT, pady=10, padx=10, state=ACTIVE)
Button2 = Button(top, text="Rectangle", command=click2, relief=GROOVE, bg="Maroon", fg="Violet",
                 activebackground="Violet", activeforeground="Maroon", justify=CENTER, pady=10, padx=10, state=ACTIVE)
Button1 = Button(top, text="Line", command=click1, relief=GROOVE, bg="yellow", fg="pink",
                 activebackground="pink", activeforeground="yellow", justify=RIGHT, padx=10, pady=10, state=ACTIVE)
Button = Button(top, text="Arc", command=click, relief=GROOVE, bg="red", fg="blue",
                activebackground="blue", activeforeground="red", justify=LEFT, padx=10, pady=10, state=ACTIVE)
Button.flash()
Button.place(x=10, y=10)
Button1.place(x=150, y=10)
Button2.place(x=10, y=70)
Button3.place(x=110, y=71)
Button4.place(x=70, y=10)

top.mainloop()
