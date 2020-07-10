from tkinter import *
from tkinter import messagebox
import math

top = Tk()
top.title("Calculater")
top.minsize(750, 450)
o1 = []
o2 = []
h = 0
w = ""
img = PhotoImage(file="delete-512.png")
photo = img.subsample(17, 17)


expression = ''


def click(num):
    c = L["text"]
    c = str(c)
    global expression
    expression = c+str(num)
    L.config(text=expression, font="bold")
    button_7.config(text="7", font="bold", command=lambda: click("7"))
    button_8.config(text="8", font="bold", command=lambda: click("8"))
    button_9.config(text="9", font="bold", command=lambda: click("9"))
    button_6.config(text="6", font="bold", command=lambda: click("6"))
    button_5.config(text="5", font="bold", command=lambda: click("5"))
    button_4.config(text="4", font="bold", command=lambda: click("4"))
    button_3.config(text="3", font="bold", command=lambda: click("3"))
    button_2.config(text="2", font="bold", command=lambda: click("2"))
    button_1.config(text="1", font="bold", command=lambda: click("1"))
    button_0.config(text="0", font="bold", command=lambda: click("0"))


def click2(sym):
    c = L["text"]
    c = str(c)
    if c[-1] == '/' or c[-1] == '*' or c[-1] == '-' or c[-1] == '+':
        global expression
        c1 = c[-1]
        c = c.replace(c1, sym)
        # expression = c + str(sym)
        L.config(text=c, font="bold")
        button_7.config(text="7", font="bold", command=lambda: click("7"))
        button_8.config(text="8", font="bold", command=lambda: click("8"))
        button_9.config(text="9", font="bold", command=lambda: click("9"))
        button_6.config(text="6", font="bold", command=lambda: click("6"))
        button_5.config(text="5", font="bold", command=lambda: click("5"))
        button_4.config(text="4", font="bold", command=lambda: click("4"))
        button_3.config(text="3", font="bold", command=lambda: click("3"))
        button_2.config(text="2", font="bold", command=lambda: click("2"))
        button_1.config(text="1", font="bold", command=lambda: click("1"))
        button_0.config(text="0", font="bold", command=lambda: click("0"))

    else:
        expression = c + str(sym)
        L.config(text=expression, font="bold")
        button_7.config(text="7", font="bold", command=lambda: click("7"))
        button_8.config(text="8", font="bold", command=lambda: click("8"))
        button_9.config(text="9", font="bold", command=lambda: click("9"))
        button_6.config(text="6", font="bold", command=lambda: click("6"))
        button_5.config(text="5", font="bold", command=lambda: click("5"))
        button_4.config(text="4", font="bold", command=lambda: click("4"))
        button_3.config(text="3", font="bold", command=lambda: click("3"))
        button_2.config(text="2", font="bold", command=lambda: click("2"))
        button_1.config(text="1", font="bold", command=lambda: click("1"))
        button_0.config(text="0", font="bold", command=lambda: click("0"))


def clear():
    global expression
    expression = ''
    L.config(text="0", font="bold")
    L6.config(text=expression, font="bold")
    button_7.config(command=lambda: click("7"))
    button_8.config(command=lambda: click("8"))
    button_9.config(command=lambda: click("9"))
    button_6.config(command=lambda: click("6"))
    button_5.config(command=lambda: click("5"))
    button_4.config(command=lambda: click("4"))
    button_3.config(command=lambda: click("3"))
    button_2.config(command=lambda: click("2"))
    button_1.config(command=lambda: click("1"))
    button_0.config(command=lambda: click("0"))
    button_mul.config(command=lambda: click2("*"))
    button_div.config(command=lambda: click2("/"))
    button_add.config(command=lambda: click2("+"))
    button_sub.config(command=lambda: click2("-"))
    button_sqrt.config(command=square)
    button_sqr.config(command=lambda: power)
    button_div_x.config(command=lambda: comp)


def power():
    global expression
    expression = expression + "^"
    L.config(text=expression, font="bold")
    b = L["text"]
    b2 = L6["text"]
    b1 = "{} = ".format(b)
    L6.config(text=b1)
    if L["text"]  == "0":
        L6.config(text="0 = ")
        L.config(text="0")
    try:
        if "^" in expression:
            if "^" == expression[-1]:
                new_expression = "(" + expression[:-1] + ")" + "**" + "2"
                print(new_expression)
                expression = new_expression
                total = str(eval(expression))
                L.config(text=total, font="bold")
                # expression = ''
                # L6.config(text=total1)
                b3 = "{} = {}".format(b, total)
                add(b3)
                button_7.config(command=lambda: command("7"))
                button_8.config(command=lambda: command("8"))
                button_9.config(command=lambda: command("9"))
                button_6.config(command=lambda: command("6"))
                button_5.config(command=lambda: command("5"))
                button_4.config(command=lambda: command("4"))
                button_3.config(command=lambda: command("3"))
                button_2.config(command=lambda: command("2"))
                button_1.config(command=lambda: command("1"))
                button_0.config(command=lambda: command("0"))
            else:
                expression.split("^")
                print(expression[0][:-1])
                new_expression = "(" + "(" + expression[0][-1] + ")" + "**" + "2" + ")" + expression[1][0] + "(" + expression[-1:] + ")"
                print(new_expression)
                expression = new_expression
                total = str(eval(expression))
                L.config(text=total, font="bold")
                b1 = "{} = {}".format(b, total)
                add(b1)
                button_7.config(command=lambda: command("7"))
                button_8.config(command=lambda: command("8"))
                button_9.config(command=lambda: command("9"))
                button_6.config(command=lambda: command("6"))
                button_5.config(command=lambda: command("5"))
                button_4.config(command=lambda: command("4"))
                button_3.config(command=lambda: command("3"))
                button_2.config(command=lambda: command("2"))
                button_1.config(command=lambda: command("1"))
                button_0.config(command=lambda: command("0"))
    except:
        e = "{} = Error".format(b)
        add(e)
        L.config(text="Error", font="bold")
        # expression = ''
        button_7.config(command=lambda: command("7"))
        button_8.config(command=lambda: command("8"))
        button_9.config(command=lambda: command("9"))
        button_6.config(command=lambda: command("6"))
        button_5.config(command=lambda: command("5"))
        button_4.config(command=lambda: command("4"))
        button_3.config(command=lambda: command("3"))
        button_2.config(command=lambda: command("2"))
        button_1.config(command=lambda: command("1"))
        button_0.config(command=lambda: command("0"))


def square():
    try:
        a = L["text"]
        total = str(eval(a))
        total1 = "(" + total + ")" + "**0.5"
        total2 = str(eval(total1))
        L6.config(text="√"+a+" =")
        L.config(text=total2)
        button_7.config(command=lambda: command("7"))
        button_8.config(command=lambda: command("8"))
        button_9.config(command=lambda: command("9"))
        button_6.config(command=lambda: command("6"))
        button_5.config(command=lambda: command("5"))
        button_4.config(command=lambda: command("4"))
        button_3.config(command=lambda: command("3"))
        button_2.config(command=lambda: command("2"))
        button_1.config(command=lambda: command("1"))
        button_0.config(command=lambda: command("0"))
        button_mul.config(command=lambda: click2("*"))
        button_div.config(command=lambda: click2("/"))
        button_add.config(command=lambda: click2("+"))
        button_sub.config(command=lambda: click2("-"))
        button_sqrt.config(command=square)
        c = "{}  {}".format(L6["text"], total2)
        add(c)
        if a[-1] == "√":
            a.replace(a[-1], "")
            a1 = L["text"]
            total = str(eval(a1))
            total1 = "(" + total + ")" + "**0.5"
            total2 = str(eval(total1))
            L6.config(text="√" + a + " =")
            L.config(text=total2)
            button_7.config(command=lambda: command("7"))
            button_8.config(command=lambda: command("8"))
            button_9.config(command=lambda: command("9"))
            button_6.config(command=lambda: command("6"))
            button_5.config(command=lambda: command("5"))
            button_4.config(command=lambda: command("4"))
            button_3.config(command=lambda: command("3"))
            button_2.config(command=lambda: command("2"))
            button_1.config(command=lambda: command("1"))
            button_0.config(command=lambda: command("0"))
            button_mul.config(command=lambda: click2("*"))
            button_div.config(command=lambda: click2("/"))
            button_add.config(command=lambda: click2("+"))
            button_sub.config(command=lambda: click2("-"))
            button_sqrt.config(command=square)
            c = "{} = {}".format(L6["text"], total1)
            add(c)
    except:
        if L["text"] == "":
            L.config(text="Error", font="bold")
            # expression = ''
            button_7.config(command=lambda: command("7"))
            button_8.config(command=lambda: command("8"))
            button_9.config(command=lambda: command("9"))
            button_6.config(command=lambda: command("6"))
            button_5.config(command=lambda: command("5"))
            button_4.config(command=lambda: command("4"))
            button_3.config(command=lambda: command("3"))
            button_2.config(command=lambda: command("2"))
            button_1.config(command=lambda: command("1"))
            button_0.config(command=lambda: command("0"))
            button_mul.config(command=lambda: click2("*"))
            button_div.config(command=lambda: click2("/"))
            button_add.config(command=lambda: click2("+"))
            button_sub.config(command=lambda: click2("-"))
            button_sqrt.config(command=square)
        else:
            e = "{} = Error".format(a)
            add(e)
            L.config(text="Error", font="bold")
            # expression = ''
            button_7.config(command=lambda: command("7"))
            button_8.config(command=lambda: command("8"))
            button_9.config(command=lambda: command("9"))
            button_6.config(command=lambda: command("6"))
            button_5.config(command=lambda: command("5"))
            button_4.config(command=lambda: command("4"))
            button_3.config(command=lambda: command("3"))
            button_2.config(command=lambda: command("2"))
            button_1.config(command=lambda: command("1"))
            button_0.config(command=lambda: command("0"))
            button_mul.config(command=lambda: click2("*"))
            button_div.config(command=lambda: click2("/"))
            button_add.config(command=lambda: click2("+"))
            button_sub.config(command=lambda: click2("-"))
            button_sqrt.config(command=square)


def comp():
    a = L["text"]
    a = str(a)
    total = str(eval(a))
    L6.config(text="1/"+total)
    total = float(total)
    total1 = 1/total
    L.config(text=total1)
    button_mul.config(command=lambda: click("*"))
    button_div.config(command=lambda: click("/"))
    button_add.config(command=lambda: click("+"))
    button_sub.config(command=lambda: click("-"))
    button_sqrt.config(command=square)
    button_sqr.config(command=power)
    button_7.config(command=lambda: command("7"))
    button_8.config(command=lambda: command("8"))
    button_9.config(command=lambda: command("9"))
    button_6.config(command=lambda: command("6"))
    button_5.config(command=lambda: command("5"))
    button_4.config(command=lambda: command("4"))
    button_3.config(command=lambda: command("3"))
    button_2.config(command=lambda: command("2"))
    button_1.config(command=lambda: command("1"))
    button_0.config(command=lambda: command("0"))


def add_button():
    button_7.config(command=lambda: command("7"))
    button_8.config(command=lambda: command("8"))
    button_9.config(command=lambda: command("9"))
    button_6.config(command=lambda: command("6"))
    button_5.config(command=lambda: command("5"))
    button_4.config(command=lambda: command("4"))
    button_3.config(command=lambda: command("3"))
    button_2.config(command=lambda: command("2"))
    button_1.config(command=lambda: command("1"))
    button_0.config(command=lambda: command("0"))
    button_mul.config(command=lambda: click2("*"))
    button_div.config(command=lambda: click2("/"))
    button_add.config(command=lambda: click2("+"))
    button_sub.config(command=lambda: click2("-"))
    button_sqrt.config(command=square)
    button_sqr.config(command=lambda: power)
    button_div_x.config(command=lambda: comp)


def equal_press():
    global expression
    b = L["text"]
    b1 = "{} = ".format(b)
    L6.config(text=b1)
    try:
        total = str(eval(expression))
        L.config(text=total, font="bold")
        expression = str(total)
        b1 = "{} = {}".format(b, total)
        add(b1)
        add_button()
        if "%" in expression:
            total = b.split("%")
            total0 = str(eval(total[0]))
            total1 = str(eval(total[1]))
            total0 = float(total0)
            total1 = float(total1)
            total2 = total0%total1
            L6.config(text=b)
            L.config(text=total2)
            button_mul.config(command=lambda: click2("*"))
            button_div.config(command=lambda: click2("/"))
            button_add.config(command=lambda: click("+"))
            button_sub.config(command=lambda: click2("-"))
            button_sqrt.config(command=square)
            button_sqr.config(command=power)
            button_div_x.config(command=lambda: click("/x"))
    except:
        e = "{} = Error".format(b)
        add(e)

        L.config(text="Error", font="bold")
        # expression = ''
        button_7.config(command=lambda: command("7"))
        button_8.config(command=lambda: command("8"))
        button_9.config(command=lambda: command("9"))
        button_6.config(command=lambda: command("6"))
        button_5.config(command=lambda: command("5"))
        button_4.config(command=lambda: command("4"))
        button_3.config(command=lambda: command("3"))
        button_2.config(command=lambda: command("2"))
        button_1.config(command=lambda: command("1"))
        button_0.config(command=lambda: command("0"))


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
        s1 = Scrollbar(top1, orient=VERTICAL)
        s1.pack(side=RIGHT, fill=Y)
        s2 = Scrollbar(top1, orient=HORIZONTAL)
        s2.pack(side=BOTTOM, fill=BOTH)
        L5 = Listbox(top1, width=42, height=30, yscrollcommand=s1.set, xscrollcommand=s2.set)
        for y in range(len(o1)):
            L5.insert(END, o1[y]+"  ")
        s1.config(command=L5.yview)
        s2.config(command=L5.xview)
        L5.pack(side=LEFT, fill=BOTH)
        top1.resizable(height=False, width=False)
        top1.mainloop()


def m_plus():
    o2.reverse()
    print(o2)
    b = o2[0]
    a = L["text"]
    total = str(eval(a))
    total = float(total)
    b = float(b)
    total1 = b+total
    language.config(text=total1)


def memory():

    global o2
    top2 = Tk()
    top2.title("Memory")
    if o2 == []:
        top2.minsize(200, 200)
        L4 = Label(top2, text="There is nothing in your Memory yet")
        L4.pack()
        top2.resizable(height=False, width=False)
        top2.mainloop()
    else:
        top2.minsize(200, 400)
        for y in range(len(o2)):
            languages1 = Menubutton(top2, text=o2[y], width=40, bg="white", activebackground="grey")
            options = Menu(languages1)
            languages1.config(menu=options)
            options.add_command(label='MC')
            options.add_command(label='M+')
            options.add_command(label='M-')
            languages1.pack(side=BOTTOM)
        top2.resizable(height=False, width=False)
        top2.mainloop()


def add(result):
    global o1
    o1.append(result)


def add1():
    global h
    h = h + 1
    if h == 20:
        messagebox.showerror("Error", "Memory space full\nPlease clear some Memory")
        button_memory1.config(state=DISABLED)
    global o2
    a = L["text"]
    try:
        if a[29] == "1" or a[29] == "2" or a[29] == "3" or a[29] == "4" or a[29] == "5" or a[29] == "6" or a[29] == "7" or a[29] == "8" or a[29] == "9" or a[29] == "10" :
            messagebox.showerror("Error", "Cannot store more than 30 numbers")
            x = messagebox.askquestion("Question", "Do you want to store first 30")
            c = ""
            if x == "yes":
                for i in range(30):
                    c = c+a[i]
                o2.append(c)
    except:
        if "*" or "/" or "+" or "-" or "%" in a:
            try:
                total = str(eval(a))
                o2.append(total)

            except:
                messagebox.showwarning("Warning", "The calculation you have enter has a syntax error \nPlease "
                                                  "enter again")
                L.config(text="")
                L6.config(text="")


def delete():
    a = L["text"]
    d = L6["text"]
    if L["text"] == "":
        L6.config(text="")
        button_7.config(command=lambda: click("7"))
        button_8.config(command=lambda: click("8"))
        button_9.config(command=lambda: click("9"))
        button_6.config(command=lambda: click("6"))
        button_5.config(command=lambda: click("5"))
        button_4.config(command=lambda: click("4"))
        button_3.config(command=lambda: click("3"))
        button_2.config(command=lambda: click("2"))
        button_1.config(command=lambda: click("1"))
        button_0.config(command=lambda: click("0"))
        button_mul.config(command=lambda: click2("*"))
        button_div.config(command=lambda: click2("/"))
        button_add.config(command=lambda: click2("+"))
        button_sub.config(command=lambda: click2("-"))
        button_sqrt.config(command=square)
        button_sqr.config(command=lambda: power)
        button_div_x.config(command=lambda: comp)
    total = str(eval(d))
    if total != a:
        L6.config(text=total)
        button_7.config(command=lambda: click("7"))
        button_8.config(command=lambda: click("8"))
        button_9.config(command=lambda: click("9"))
        button_6.config(command=lambda: click("6"))
        button_5.config(command=lambda: click("5"))
        button_4.config(command=lambda: click("4"))
        button_3.config(command=lambda: click("3"))
        button_2.config(command=lambda: click("2"))
        button_1.config(command=lambda: click("1"))
        button_0.config(command=lambda: click("0"))
        button_mul.config(command=lambda: click2("*"))
        button_div.config(command=lambda: click2("/"))
        button_add.config(command=lambda: click2("+"))
        button_sub.config(command=lambda: click2("-"))
        button_sqrt.config(command=square)
        button_sqr.config(command=lambda: power)
        button_div_x.config(command=lambda: comp)
    global expression
    expression = expression[:len(a)-1]
    L.config(text=expression, font='bold')
    button_7.config(command=lambda: click("7"))
    button_8.config(command=lambda: click("8"))
    button_9.config(command=lambda: click("9"))
    button_6.config(command=lambda: click("6"))
    button_5.config(command=lambda: click("5"))
    button_4.config(command=lambda: click("4"))
    button_3.config(command=lambda: click("3"))
    button_2.config(command=lambda: click("2"))
    button_1.config(command=lambda: click("1"))
    button_0.config(command=lambda: click("0"))
    button_mul.config(command=lambda: click2("*"))
    button_div.config(command=lambda: click2("/"))
    button_add.config(command=lambda: click2("+"))
    button_sub.config(command=lambda: click2("-"))
    button_sqrt.config(command=square)
    button_sqr.config(command=lambda: power)
    button_div_x.config(command=lambda: comp)


def button():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1)


def command(number):
    b = L["text"]
    L6.config(text="Answer: "+b)
    number = str(number)
    L.config(text=number)
    expression = number
    button_7.config(text="7", font="bold", command=lambda: click("7"))
    button_8.config(text="8", font="bold", command=lambda: click("8"))
    button_9.config(text="9", font="bold", command=lambda: click("9"))
    button_6.config(text="6", font="bold", command=lambda: click("6"))
    button_5.config(text="5", font="bold", command=lambda: click("5"))
    button_4.config(text="4", font="bold", command=lambda: click("4"))
    button_3.config(text="3", font="bold", command=lambda: click("3"))
    button_2.config(text="2", font="bold", command=lambda: click("2"))
    button_1.config(text="1", font="bold", command=lambda: click("1"))
    button_0.config(text="0", font="bold", command=lambda: click("0"))
    button_div.config(state=NORMAL)
    button_mul.config(state=NORMAL)
    button_sub.config(state=NORMAL)
    button_add.config(state=NORMAL)
    button_mod.config(state=NORMAL)
    button_sqr.config(state=NORMAL)
    button_sqrt.config(state=NORMAL)
    button_equal.config(state=NORMAL)
    L6.config(text="")


button_7 = button()
button_7.config(text="7", font="bold", command=lambda: command(7))
button_7.place(x=10, y=190)

button_8 = button()
button_8.config(text="8", font="bold", command=lambda: command(8))
button_8.place(x=130, y=190)

button_9 = button()
button_9.config(text="9", font="bold", command=lambda: command(9))
button_9.place(x=250, y=190)

button_4 = button()
button_4.config(text="4", font="bold", command=lambda: command(4))
button_4.place(x=10, y=252)

button_5 = button()
button_5.config(text="5", font="bold", command=lambda: command(5))
button_5.place(x=130, y=252)

button_6 = button()
button_6.config(text="6", font="bold", command=lambda: command(6))
button_6.place(x=250, y=252)

button_1 = button()
button_1.config(text="1", font="bold", command=lambda: command(1))
button_1.place(x=10, y=314)

button_2 = button()
button_2.config(text="2", font="bold", command=lambda: command(2))
button_2.place(x=130, y=314)

button_3 = button()
button_3.config(text="3", font="bold", command=lambda: command(3))
button_3.place(x=250, y=314)

button_0 = button()
button_0.config(text="0", font="bold", command=lambda: command(0))
button_0.place(x=130, y=376)

button_c = button()
button_c.config(text="C", font="bold", command=clear)
button_c.place(x=10, y=376)

button_d = button()
button_d.config(image=photo, font="bold", compound=CENTER, width=112, height=55, command=delete)
button_d.place(x=250, y=376)

button_mul = button()
button_mul.config(text="*", font="bold", bg="grey", fg="white", command=lambda: click2("*"))
button_mul.place(x=370, y=190)

button_div = button()
button_div.config(text="/", font="bold", bg="grey", fg="white", command=lambda: click2("/"))
button_div.place(x=370, y=252)

button_add = button()
button_add.config(text="+", font="bold", bg="grey", fg="white", command=lambda: click2("+"))
button_add.place(x=370, y=314)

button_sub = button()
button_sub.config(text="-", font="bold", bg="grey", fg="white", command=lambda: click2("-"))
button_sub.place(x=370, y=376)

button_sqrt = button()
button_sqrt.config(text="√", font="bold", bg="grey", fg="white", command= square)
button_sqrt.place(x=490, y=190)

button_sqr = button()
button_sqr.config(text="^", font="bold", bg="grey", fg="white", command=power)
button_sqr.place(x=490, y=252)

button_mod = button()
button_mod.config(text="mod", font="bold", bg="grey", fg="white", command=lambda: click("%"))
button_mod.place(x=490, y=314)

button_div_x = button()
button_div_x.config(text="1/x", font="bold", bg="grey", fg="white", command=comp)
button_div_x.place(x=490, y=376)

button_equal = button()
button_equal.config(text="=", font="bold", bg="grey", fg="white", height=10, command=equal_press)
button_equal.place(x=610, y=191)

M = Menu(top)
M1 = Menu(M, tearoff=0)
M1.add_command(label="Exit", command=top.quit)
M1.add_command(label="Memory", command=memory)
M1.add_command(label="History", command=history)
M.add_cascade(label="Menu", menu=M1)
top.config(menu=M)
L = Label(top, text="0", justify=RIGHT, font="bold")
L6 = Label(top, text="", fg="grey", font=5)
L6.place(relx=1.0, rely=0.0, anchor="ne")
L.place(relx=1.0, rely=0.1, anchor="ne")
top.resizable(height=False, width=False)
button_memory = button()
button_memory.config(text="M+", width=10, command=m_plus)
button_memory.place(x=10, y=147)

button_memory1 = button()
button_memory1.config(text="M", width=10, command=add1)
button_memory1.place(x=90, y=147)

button_memory2 = button()
button_memory2.config(text="M-", width=10)
button_memory2.place(x=170, y=147)

button_memory3 = button()
button_memory3.config(text="MR", width=10)
button_memory3.place(x=250, y=147)

button_memory4 = button()
button_memory4.config(text="MC", width=10)
button_memory4.place(x=330, y=147)
top.mainloop()