from tkinter import *
from tkinter import messagebox


top = Tk()
top.title("Calculater")
top.minsize(620, 450)
o1 = []
w = ""
img = PhotoImage(file="delete-512.png")
photo = img.subsample(17, 17)
# expression = ''


# def click(num):
#     global expression
#     expression = expression+str(num)
#     return expression


def click0():
    a = L['text']
    L.config(text=a+"0", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click1():
    a = L['text']
    L.config(text=a+"1", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click2():
    a = L['text']
    L.config(text=a+"2", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click3():
    a = L['text']
    L.config(text=a+"3", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click4():
    a = L['text']
    L.config(text=a+"4", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click5():
    a = L['text']
    L.config(text=a+"5", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click6():
    a = L['text']
    L.config(text=a+"6", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click7():
    a = L['text']
    L.config(text=a+"7", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click8():
    a = L['text']
    L.config(text=a+"8", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click9():
    a = L['text']
    L.config(text=a+"9", font="bold")
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)


def click_():
    a = L['text']
    if L6["text"] == "":
        L.config(text=a + "*", font="bold")
        b11.config(state=ACTIVE, command=delete)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)

        b.config(command=click7)
        b1.config(command=click8)
        b2.config(command=click9)
        b3.config(command=click4)
        b4.config(command=click5)
        b5.config(command=click6)
        b6.config(command=click1)
        b7.config(command=click2)
        b8.config(command=click3)
        b9.config(command=click0)
        b11.config(state=ACTIVE, command=delete)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)

        b.config(command=click7)
        b1.config(command=click8)
        b2.config(command=click9)
        b3.config(command=click4)
        b4.config(command=click5)
        b5.config(command=click6)
        b6.config(command=click1)
        b7.config(command=click2)
        b8.config(command=click3)
        b9.config(command=click0)

def click__():
    a = L['text']
    if L6["text"] == "":
        L.config(text=a+"/", font="bold")
        b11.config(state=ACTIVE, command=delete)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)

        b.config(command=click7)
        b1.config(command=click8)
        b2.config(command=click9)
        b3.config(command=click4)
        b4.config(command=click5)
        b5.config(command=click6)
        b6.config(command=click1)
        b7.config(command=click2)
        b8.config(command=click3)
        b9.config(command=click0)
        b11.config(state=ACTIVE, command=delete)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)

        b.config(command=click7)
        b1.config(command=click8)
        b2.config(command=click9)
        b3.config(command=click4)
        b4.config(command=click5)
        b5.config(command=click6)
        b6.config(command=click1)
        b7.config(command=click2)
        b8.config(command=click3)
        b9.config(command=click0)


def click___():
    a = L['text']
    if L6["text"] == "":
        L.config(text=a+"+", font="bold")
        b9.config(command=click0)
        b11.config(state=ACTIVE, command=delete)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)

        b.config(command=click7)
        b1.config(command=click8)
        b2.config(command=click9)
        b3.config(command=click4)
        b4.config(command=click5)
        b5.config(command=click6)
        b6.config(command=click1)
        b7.config(command=click2)
        b8.config(command=click3)
        b9.config(command=click0)


def click____():
    a = L['text']
    L.config(text=a+"-", font="bold")
    b11.config(state=ACTIVE, command=delete)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)

    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)


def click_____():
    global result3
    result = L["text"]
    print(result)
    # add(result)
    d=[]
    for i in range(len(result)):
        d.append(i)
    d.reverse()
    if d[0] == ".":
        d.remove(d[0])
        s=""
        for y in d:
            s=s+y
        L.config(text=s)
        L.config(text="")
        b11.config(state=ACTIVE)
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)
    print(result)
    p = "+"
    m = "*"
    d = "/"
    s = "-"
    if p in result:
        global L6
        q = "{} =".format(result)
        L6.config(text=q)
        result1 = 0
        a = result.split(p)
        for i in a:
            i = float(i)
            result1 = i + result1
        result3 = str(result1)
        L.config(text=result3)
        L.config(text=result3)
        b.config(command=command7)
        b1.config(command=command8)
        b2.config(command=command9)
        b3.config(command=command4)
        b4.config(command=command5)
        b5.config(command=command6)
        b6.config(command=command1)
        b7.config(command=command2)
        b8.config(command=command3)
        b9.config(command=command)
        result4 = "{} = {}".format(result, result3)
        add(result4)
        b11.config(state=DISABLED, disabledforeground="black")
    elif s in result:
        # global L6
        q = "{} =".format(result)
        L6.config(text=q)
        result1 = 0
        a = result.split(s)
        for i in a:
            i = float(i)
            print(i)
            result1 = i + result1
            # a.remove(i)
            break
        result2 = a[1]
        result2 = int(result2)
        result3 = result1 - result2
        result3 = str(result3)
        L.config(text=result3)
        b.config(command=command7)
        b1.config(command=command8)
        b2.config(command=command9)
        b3.config(command=command4)
        b4.config(command=command5)
        b5.config(command=command6)
        b6.config(command=command1)
        b7.config(command=command2)
        b8.config(command=command3)
        b9.config(command=command)
        result4 = "{} = {}".format(result, result3)
        add(result4)
        b11.config(state=DISABLED, disabledforeground="black")

    elif m in result:
        # global L6
        q = "{} =".format(result)
        L6.config(text=q)
        result1 = 0
        a = result.split(m)
        for i in a:
            i = float(i)
            result1 = i + result1
            break
        result2 = a[1]
        result2 = int(result2)
        result3 = result1 * result2
        result3 = str(result3)
        L.config(text=result3)
        b.config(command=command7)
        b1.config(command=command8)
        b2.config(command=command9)
        b3.config(command=command4)
        b4.config(command=command5)
        b5.config(command=command6)
        b6.config(command=command1)
        b7.config(command=command2)
        b8.config(command=command3)
        b9.config(command=command)
        result4 = "{} = {}".format(result, result3)
        add(result4)
        b11.config(state=DISABLED, disabledforeground="black")

    elif d in result:
        # global L6
        q = "{} =".format(result)
        L6.config(text=q)
        try:
            result1 = 0
            a = result.split(d)
            # print(a[1])

            for i in a:
                i = float(i)
                result1 = i + result1
                break
            result2 = a[1]
            result2 = int(result2)
            result3 = result1/result2
            result3 = str(result3)
            L.config(text=result3)
            L.config(text=result3)
            b.config(command=command7)
            b1.config(command=command8)
            b2.config(command=command9)
            b3.config(command=command4)
            b4.config(command=command5)
            b5.config(command=command6)
            b6.config(command=command1)
            b7.config(command=command2)
            b8.config(command=command3)
            b9.config(command=command)
            result4 = "{} = {}".format(result, result3)
            add(result4)
            b11.config(state=DISABLED, disabledforeground="black")
        except:
            messagebox.showerror("Error", "Wrong Division Entered\nTry again")
            result1 = "{} = Infinity".format(result)
            add(result1)
            L.config(text="")
    else:
        L.config(text=result)


def command7():
    global result3
    L.config(text="7")
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)

    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE)
    w = "Answer:{}".format(result3, command=delete)
    L6.config(text=w)


def command8():
    global result3
    L.config(text="8")
    b1.config(command=click8)
    b.config(command=click7)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)

    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command9():
    global result3
    L.config(text="9")
    b2.config(command=click9)
    b.config(command=click7)
    b1.config(command=click8)
    # b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)

    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command4():
    global result3
    L.config(text="4")
    b3.config(command=click4)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    # b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)

    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE)
    w = "Answer:{}".format(result3, command=delete)
    L6.config(text=w)


def command5():
    global result3
    L.config(text="5")
    b4.config(command=click5)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    # b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command6():
    global result3
    L.config(text="6")
    b5.config(command=click6)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    # b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command1():
    global result3
    L.config(text="1")
    b6.config(command=click1)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    # b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command2():
    global result3
    L.config(text="2")
    b7.config(command=click2)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    # b7.config(command=click2)
    b8.config(command=click3)
    b9.config(command=click0)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command3():
    global result3
    L.config(text="3")
    b8.config(command=click3)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b9.config(command=click0)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def command():
    global result3
    L.config(text="0")
    b9.config(command=click0)
    b.config(command=click7)
    b1.config(command=click8)
    b2.config(command=click9)
    b3.config(command=click4)
    b4.config(command=click5)
    b5.config(command=click6)
    b6.config(command=click1)
    b7.config(command=click2)
    b8.config(command=click3)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b11.config(state=ACTIVE, command=delete)
    w = "Answer:{}".format(result3)
    L6.config(text=w)


def clear():
    L.config(text="")
    a = L6["text"]
    L6.config(text="")
    L.config(text="")
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    # try:
    #     if a[0] != "A":
    #         L6.config(text="")
    #         b12.config(state=DISABLED)
    #         b13.config(state=DISABLED)
    #         b14.config(state=DISABLED)
    #         b15.config(state=DISABLED)
    #         b16.config(state=DISABLED)
    #     else:
    #         b12.config(state=DISABLED)
    #         b13.config(state=DISABLED)
    #         b14.config(state=DISABLED)
    #         b15.config(state=DISABLED)
    #         b16.config(state=DISABLED)
    # except:
    #     b12.config(state=DISABLED)
    #     b13.config(state=DISABLED)
    #     b14.config(state=DISABLED)
    #     b15.config(state=DISABLED)
    #     b16.config(state=DISABLED)


def delete():
    try:
        text = L["text"]
        b = []
        for i in range(len(text)):
            b.append(text[i])
        b.reverse()
        d = b[0]
        b.remove(d)
        b.reverse()
        s = ""
        for j in b:
            s = s+j
        L.config(text=s)
        if s == "":
            b12.config(state=DISABLED)
            b13.config(state=DISABLED)
            b14.config(state=DISABLED)
            b15.config(state=DISABLED)
            b16.config(state=DISABLED)
        if L["text"] == "":
            L6.config(text="")
        text1 = L["text"]
        m = "*"
        d1 = "/"
        a = "+"
        s1 = "-"
        d=[]
        for y in range(len(text1)):
            d.append(text1[y])
        d.reverse()
        if d[0] == m:
            b12.config(state=DISABLED)
            b13.config(state=DISABLED)
            b14.config(state=DISABLED)
            b15.config(state=DISABLED)
            b16.config(state=DISABLED)
        elif d[0] == d1:
            b12.config(state=DISABLED)
            b13.config(state=DISABLED)
            b14.config(state=DISABLED)
            b15.config(state=DISABLED)
            b16.config(state=DISABLED)
        elif d[0] == s1:
            b12.config(state=DISABLED)
            b13.config(state=DISABLED)
            b14.config(state=DISABLED)
            b15.config(state=DISABLED)
            b16.config(state=DISABLED)
        elif d[0] == a:
            b12.config(state=DISABLED)
            b13.config(state=DISABLED)
            b14.config(state=DISABLED)
            b15.config(state=DISABLED)
            b16.config(state=DISABLED)
        elif d[0] == "9" or d[0] == "8" or d[0] == "7" or d[0] == "6" or d[0] == "5" or d[0] == "4"\
             or d[0] == "3" or d[0] == "2" or d[0] == "1" or d[0] == "0":
            b12.config(state=ACTIVE)
            b13.config(state=ACTIVE)
            b14.config(state=ACTIVE)
            b15.config(state=ACTIVE)
            b16.config(state=ACTIVE)


    except:
        b12.config(state=DISABLED)
        b13.config(state=DISABLED)
        b14.config(state=DISABLED)
        b15.config(state=DISABLED)
        b16.config(state=DISABLED)





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


def button0():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click0)


def button1():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click1)


def button2():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click2)


def button3():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click3)


def button4():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click4)


def button5():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click5)


def button6():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click6)


def button7():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click7)


def button8():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click8)


def button9():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click9)


def button_():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click0)


def button__():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click0)


def button___():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click0)


def button____():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click0)


def button_____():
    return Button(top, padx=1, bg="white", width=10, height=2, text="  ", border=1, command=click_____)


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
b3.place(x=10,  y=252)

b4 = button5()
b4.config(text="5", font="bold")
b4.place(x=130,  y=252)

b5 = button6()
b5.config(text="6", font="bold")
b5.place(x=250,  y=252)

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
b11.config(image=photo, font="bold", command=delete, compound=CENTER, width=112, height=55)
b11.place(x=250, y=376)

b12 = button_()
b12.config(text="*", font="bold", bg="grey", fg="white", command=click_, state=DISABLED)
b12.place(x=370, y=190)


b14 = button__()
b14.config(text="/", font="bold", bg="grey", fg="white", command=click__, state=DISABLED)
b14.place(x=370,  y=252)


b13 = button___()
b13.config(text="+", font="bold", bg="grey", fg="white", command=click___, state=DISABLED)
b13.place(x=370, y=314)

b15 = button____()
b15.config(text="-", font="bold", bg="grey", fg="white", command=click____, state=DISABLED)
b15.place(x=370, y=376)

b16 = button_____()
b16.config(text="=", font="bold", bg="grey", fg="white", height=10, state=DISABLED)
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