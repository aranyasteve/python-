from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Calculator")
top.minsize(650, 400)
o1 = []
o2 = []
h = 0
w = ""
img = PhotoImage(file="delete-512.png")
img1 = PhotoImage(file='calccc.png')
top.iconphoto(False, img1)
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
    button_d.config(state=NORMAL)


def click2(sym):
    try:
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
            button_d.config(state=NORMAL)

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
            button_d.config(state=NORMAL)
    except:
        L.confing(text="")
        button_d.config(state=DISABLED)


def clear():
    global expression
    expression = ''
    L.config(text="0", font="bold")
    L6.config(text=expression, font="bold")
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
    button_d.config(state=DISABLED)


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
    button_d.config(state=NORMAL)


def equal_press():
    global expression
    b = L["text"]
    b1 = "{} =".format(b)
    L6.config(text=b1)
    try:
        if b[-1] == "*" or "/" or "+" or "-":
            L.config(text="Error")
        total = str(eval(expression))
        L.config(text=total, font="bold")
        expression = str(total)
        b1 = "{} = {}".format(b, total)
        add(b1)
        add_button()
        button_d.config(state=NORMAL)
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
        button_d.config(state=NORMAL)


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


def add(result):
    global o1
    o1.append(result)


def delete():
    try:
        b = []
        a = L["text"]
        a = str(a)
        for i in a:
            i = str(i)
            b.append(i)
        print(b)
        if b == [] or b == ["1"] or b == ["2"] or b == ["3"] or b == ["4"] or b == ["5"] or b == ["6"]or b == ["7"] or b == ["8"] or b == ["9"] or b == ["0"]:
            L.config(text="0")
        b.reverse()
        c = b[0]
        b.remove(c)
        b.reverse()
        b.reverse()
        d = ""
        for j in range(len(b)):
            e = str(b[j])
            d = e+d
        L.config(text=d)
    except:
        b = []


def button():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1)


def command(number):
    b = L["text"]
    L6.config(text="Answer: "+b)
    number = str(number)
    L.config(text=number)
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
    button_equal.config(state=NORMAL)
    button_d.config(state=NORMAL)
    L6.config(text="")


b = button()
b.config(height=15, state=DISABLED, width=9)
b.place(x=0, y=190)
button_7 = button()
button_7.config(text="7", font="bold", command=lambda: command(7), height=2)
button_7.place(x=63, y=190)

button_8 = button()
button_8.config(text="8", font="bold", command=lambda: command(8))
button_8.place(x=180, y=190)

button_9 = button()
button_9.config(text="9", font="bold", command=lambda: command(9))
button_9.place(x=292, y=190)

button_4 = button()
button_4.config(text="4", font="bold", command=lambda: command(4))
button_4.place(x=63, y=240)

button_5 = button()
button_5.config(text="5", font="bold", command=lambda: command(5))
button_5.place(x=180, y=240)

button_6 = button()
button_6.config(text="6", font="bold", command=lambda: command(6))
button_6.place(x=292, y=240)

button_1 = button()
button_1.config(text="1", font="bold", command=lambda: command(1))
button_1.place(x=63, y=290)

button_2 = button()
button_2.config(text="2", font="bold", command=lambda: command(2))
button_2.place(x=180, y=290)

button_3 = button()
button_3.config(text="3", font="bold", command=lambda: command(3))
button_3.place(x=292, y=290)

button_0 = button()
button_0.config(text="0", font="bold", command=lambda: command(0))
button_0.place(x=180, y=350)

button_c = button()
button_c.config(text="C", font="bold", command=clear)
button_c.place(x=63, y=350)

button_d = button()
button_d.config(image=photo, font="bold", compound=CENTER, width=112, height=44, command=delete, state=DISABLED)
button_d.place(x=292, y=350)

button_mul = button()
button_mul.config(text="*", font="bold", bg="grey", fg="white", command=lambda: click2("*"))
button_mul.place(x=410, y=190)

button_div = button()
button_div.config(text="/", font="bold", bg="grey", fg="white", command=lambda: click2("/"))
button_div.place(x=410, y=240)

button_add = button()
button_add.config(text="+", font="bold", bg="grey", fg="white", command=lambda: click2("+"))
button_add.place(x=410, y=290)

button_sub = button()
button_sub.config(text="-", font="bold", bg="grey", fg="white", command=lambda: click2("-"))
button_sub.place(x=410, y=340)

button_mod = button()
button_mod.config(text=".", font="bold", bg="grey", fg="white", command=lambda: click("."))
button_mod.place(x=525, y=190)


button_equal = button()
button_equal.config(text="=", font="bold", bg="grey", fg="white", height=7, command=equal_press, pady=6)
button_equal.place(x=525, y=240)

M = Menu(top)
M1 = Menu(M, tearoff=0)
M1.add_command(label="Exit", command=top.quit)
M1.add_command(label="History", command=history)
M.add_cascade(label="Menu", menu=M1)
top.config(menu=M)
L = Label(top, text="0", justify=RIGHT, font="bold")
L6 = Label(top, text="", fg="grey", font=5)
L6.place(relx=1.0, rely=0.0, anchor="ne")
L.place(relx=1.0, rely=0.1, anchor="ne")
top.resizable(height=False, width=False)
top.mainloop()