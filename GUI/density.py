from tkinter import *
from tkinter import messagebox

top = Tk()


def check():
    try:
        a5 = a.get()
        a7 = a1.get()
        a5 = float(a5)
        a7 = float(a7)
        density()
    except:
        messagebox.showerror("Error", "Please enter a number ")


def density():
    a5 = a.get()
    a7 = a1.get()
    a5 = float(a5)
    a7 = float(a7)
    a9 = a5/a7
    top.quit()
    top1 = Tk()
    a11 = "Density is {} unit".format(a9)
    L2 = Label(top1, text=a11, font="bold", padx=10, pady=10)
    L2.pack()
    print(a11)
    top1.mainloop()


def increase():
    a5 = a.get()
    a7 = a1.get()
    a5 = float(a5)
    a7 = float(a7)
    a8 = a7/a5
    a9 = a8*100
    a10 = a9-100
    top.quit()
    top1 = Tk()
    a11 = "Percentage Increase is by {}%".format(a10)
    L2 = Label(top1, text=a11, font="bold", padx=10, pady=10)
    L2.pack()
    print(a11)
    top1.mainloop()



top.minsize(300, 200)
# top.resizable(height=False, width=False)
top.title("Calculater")
L = Label(top, text="Density Calculater")
L1 = Label(top, text="Mass")
a = Entry(top, )
L2 = Label(top, text="Volume")
a1 = Entry(top, )
b = Button(top, text="Check", width=30, height=1, relief=SUNKEN, bg="white", command=check)
L.place(x=100, y=0)
a.place(x=150, y=50)
L1.place(x=25, y=50)
a1.place(x=150, y=100)
L2.place(x=25, y=100)
b.place(x=43, y=170)
top.mainloop()

