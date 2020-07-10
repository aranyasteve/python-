from tkinter import *
from tkinter.ttk import *
from time import strftime
top=Tk()
top.title("Clock")


def time():
    str1 = strftime('%H:%M:%S %p')
    str2 = strftime("%d-%m-%y")
    lbl.config(text="Current time is : {} and Date : {}".format(str1, str2))
    # lbl1.config(text=str2)
    lbl.after(1000, time)


lbl = Label(top, font=("calibri", 40, "bold"), background="purple", foreground="white")
# lbl1 = Label(top, font=("calibri", 40, "bold"), background="purple", foreground="white")
lbl.pack(anchor=CENTER)
# lbl1.pack(anchor=CENTER)
time()
top.resizable(width=False, height=False)
top.mainloop()
