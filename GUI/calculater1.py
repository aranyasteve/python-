from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Calculater")
top.minsize(620, 450)
o1 = []
w = ""
img = PhotoImage(file="delete-512.png")
photo = img.subsample(17, 17)


expression = ''


def click(num):
    global expression
    expression = expression+str(num)
    L.config(text=expression, font="bold")


def clear():
    global expression
    expression = ''
    L.config(text=expression, font="bold")


def equal_press():
    global expression
    b = L["text"]
    try:
        total = str(eval(expression))
        L.config(text=total, font="bold")
        expression = ''
        b1 = "{} = {}".format(b, total)
        add(b1)

    except:
        L.config(text="Error", font="bold")
        expression = ''



def history():
    global o1
    top1 = Tk()
    top1.title("History")
    if o1 == []:
        top1.minsize(200, 200)
        L4 = Label(top1, text="Your Calculations will appear here")
        L4.pack()
        top1.resizable(height=False, width=False)
        top1.mainloop()
    else:
        m = Menu(top1)
        m1 = Menu(m, tearoff=0)
        m1.add_command(label="Clear all")
        m.add_cascade(label="Menu", menu=m1)
        top.config(menu=m)
        s1 = Scrollbar(top1, orient=VERTICAL)
        s1.pack(side=RIGHT, fill=Y)
        s2 = Scrollbar(top1, orient=HORIZONTAL)
        s2.pack(side=BOTTOM, fill=BOTH)
        L5 = Listbox(top1, width=42, height=30, yscrollcommand=s1.set, xscrollcommand=s2.set)
        for y in range(len(o1)):
            L5.insert(END, o1[y])
        s1.config(command=L5.yview)
        s2.config(command=L5.xview)
        L5.pack(side=LEFT, fill=BOTH)
        top1.resizable(height=False, width=False)
        top1.mainloop()


def add(result):
    global o1
    o1.append(result)
    print(o1)


def delete():
    global expression
    expression = expression[:len(expression)-1]
    L.config(text=expression, font='bold')


def button0():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(0))


def button1():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(1))


def button2():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(2))


def button3():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(3))


def button4():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(4))


def button5():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(5))


def button6():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(6))


def button7():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(7))


def button8():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(8))


def button9():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click(9))


def button_():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click("*"))


def button__():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click("/"))


def button___():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click("+"))


def button____():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=lambda: click("-"))


def button_____():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=equal_press)


def buttons():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=equal_press)



b = button7()
b.config(text="7", font="bold")
b.place(x=10, y=190)

b1 = button8()
b1.config(text="8", font="bold")
b1.place(x=130, y=190)

b2 = button9()
b2.config(text="9", font="bold")
b2.place(x=250, y=190)

b3 = button4()
b3.config(text="4", font="bold")
b3.place(x=10, y=252)

b4 = button5()
b4.config(text="5", font="bold")
b4.place(x=130, y=252)

b5 = button6()
b5.config(text="6", font="bold")
b5.place(x=250, y=252)

b6 = button1()
b6.config(text="1", font="bold")
b6.place(x=10, y=314)

b7 = button2()
b7.config(text="2", font="bold")
b7.place(x=130, y=314)

b8 = button3()
b8.config(text="3", font="bold")
b8.place(x=250, y=314)

b9 = button0()
b9.config(text="0", font="bold")
b9.place(x=130, y=376)

b10 = button0()
b10.config(text="C", font="bold", command=clear)
b10.place(x=10, y=376)

b11 = button0()
b11.config(image=photo, font="bold", compound=CENTER, width=112, height=55, command=delete)
b11.place(x=250, y=376)

b12 = button_()
b12.config(text="*", font="bold", bg="grey", fg="white")
b12.place(x=370, y=190)

b14 = button__()
b14.config(text="/", font="bold", bg="grey", fg="white")
b14.place(x=370, y=252)

b13 = button___()
b13.config(text="+", font="bold", bg="grey", fg="white")
b13.place(x=370, y=314)

b15 = button____()
b15.config(text="-", font="bold", bg="grey", fg="white")
b15.place(x=370, y=376)

b16 = button_____()
b16.config(text="=", font="bold", bg="grey", fg="white", height=10)
b16.place(x=490, y=191)

M = Menu(top)
M1 = Menu(M, tearoff=0)
M1.add_command(label="Exit", command=top.quit)
M1.add_command(label="History", command=history)
M.add_cascade(label="Menu", menu=M1)
top.config(menu=M)
L = Label(top, text="", justify=RIGHT)
L6 = Label(top, text="", fg="grey", font=5)
L6.place(relx=1.0, rely=0.0, anchor="ne")
L.place(relx=1.0, rely=0.1, anchor="ne")
top.resizable(height=False, width=False)
top.mainloop()