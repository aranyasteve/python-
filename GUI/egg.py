import tkinter
from tkinter import *

root = Tk()

L = Label(root, text="Right-click to display menu",
          width=40, height=20)
L.pack()

m = "😃"


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


L.bind("<Button-3>", do_popup)

mainloop()