from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Calculater")
top.minsize(750, 450)
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
        if "√" in expression:
            if "√" == expression[0]:
                expression = "(" + expression[1:] + ")" + "**0.5"
            else:
                exp = expression.split("√")
                new_exp = "(" + exp[0][:-1] + ")" + exp[0][-1] + "(" + exp[1] + ")" + "**0.5"
                expression = new_exp
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


def button():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1)


button_7 = button()
button_7.config(text="7", font="bold", command=lambda: click(7))
button_7.place(x=10, y=190)

button_8 = button()
button_8.config(text="8", font="bold", command=lambda: click(8))
button_8.place(x=130, y=190)

button_9 = button()
button_9.config(text="9", font="bold", command=lambda: click(9))
button_9.place(x=250, y=190)

button_4 = button()
button_4.config(text="4", font="bold", command=lambda: click(4))
button_4.place(x=10, y=252)

button_5 = button()
button_5.config(text="5", font="bold", command=lambda: click(5))
button_5.place(x=130, y=252)

button_6 = button()
button_6.config(text="6", font="bold", command=lambda: click(6))
button_6.place(x=250, y=252)

button_1 = button()
button_1.config(text="1", font="bold", command=lambda: click(1))
button_1.place(x=10, y=314)

button_2 = button()
button_2.config(text="2", font="bold", command=lambda: click(2))
button_2.place(x=130, y=314)

button_3 = button()
button_3.config(text="3", font="bold", command=lambda: click(3))
button_3.place(x=250, y=314)

button_0 = button()
button_0.config(text="0", font="bold", command=lambda: click(0))
button_0.place(x=130, y=376)

button_c = button()
button_c.config(text="C", font="bold", command=clear)
button_c.place(x=10, y=376)

button_d = button()
button_d.config(image=photo, font="bold", compound=CENTER, width=112, height=55, command=delete)
button_d.place(x=250, y=376)

button_mul = button()
button_mul.config(text="*", font="bold", bg="grey", fg="white", command=lambda: click("*"))
button_mul.place(x=370, y=190)

button_div = button()
button_div.config(text="/", font="bold", bg="grey", fg="white", command=lambda: click("/"))
button_div.place(x=370, y=252)

button_add = button()
button_add.config(text="+", font="bold", bg="grey", fg="white", command=lambda: click("+"))
button_add.place(x=370, y=314)

button_sub = button()
button_sub.config(text="-", font="bold", bg="grey", fg="white", command=lambda: click("-"))
button_sub.place(x=370, y=376)

button_sqrt = button()
button_sqrt.config(text="√", font="bold", bg="grey", fg="white", command=lambda: click("√"))
button_sqrt.place(x=490, y=190)

button_sqr = button()
button_sqr.config(text="^", font="bold", bg="grey", fg="white", command=lambda: click("^"))
button_sqr.place(x=490, y=252)

button_mod = button()
button_mod.config(text="mod", font="bold", bg="grey", fg="white", command=lambda: click("%"))
button_mod.place(x=490, y=314)

button_div_x = button()
button_div_x.config(text="1/x", font="bold", bg="grey", fg="white", command=lambda: click("/"))
button_div_x.place(x=490, y=376)

button_equal = button()
button_equal.config(text="=", font="bold", bg="grey", fg="white", height=10, command=equal_press)
button_equal.place(x=610, y=191)

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