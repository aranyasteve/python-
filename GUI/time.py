from tkinter import *
from tkinter.ttk import *
from time import strftime
top=Tk()
top.title("Clock")


def time():
    global hrs
    global min
    global sec
    global msec
    global b
    msec = msec+1

    if msec == 60:
        sec = sec+1
        msec = 0
    if msec and sec == 60:
        min = min+1
        sec = 0
        msec = 0
    if min and sec and msec == 60:
        hrs = hrs+1
        min = 0
        sec = 0
        msec = 0
    b = "{}:{}:{}:{}".format(hrs, min, sec, msec)
    lbl.config(text=b)
    lbl.after(10, time)


hrs = 00
min = 00
sec = 00
msec = 00

b = "{}:{}:{}:{}".format(hrs, min, sec, msec)
lbl = Label(top, text=b,  font=("calibri", 40, "bold"), background="purple", foreground="white")
# lbl1 = Label(top, font=("calibri", 40, "bold"), background="purple", foreground="white")
# b = Button(text="END")
# b.pack()
lbl.pack(anchor=CENTER)
# lbl1.pack(anchor=CENTER)
time()
# top.resizable(width=False, height=False)
top.mainloop()
