from tkinter import *
import time
import random
from tkinter import messagebox


top = Tk()
top.title("MineSweeper")
top.minsize(355, 490)
img = PhotoImage(file="s.png")
img1 = PhotoImage(file="m1.png")
img2 = PhotoImage(file='flag.png')
top.iconphoto(False, img1)
photo = img.subsample(17, 17)
o = []
o1 = []


def button():
    return Button(top, padx=15, pady=10,  bg="grey", relief="raised", width=1)


def time():
    global lbl
    global min
    global sec
    global b
    sec = sec+1
    if sec == 60:
        min = min+1
        sec = 0
    b = "{}:{}".format(min, sec)
    if L2["text"] == "😵":
        lbl.config(text=b)
    else:
        lbl.config(text=b)
        lbl.after(1000, time)


def click(row, col):
    global e
    try:
        e = e+1
        for i in range(row):
            for j in range(col):
                b1[row][col].config(text="", relief=SUNKEN, state=DISABLED, bg="white")
    except:
        e = e+1
        b1[row][col].config(text="", relief=SUNKEN, state=DISABLED, bg="white")


def click1(row, col, num):
    global e
    if num == 0:
        b1[row][col].config(activebackground="white",  relief=SUNKEN, state=DISABLED, bg="white")
        click(row, col)
        b1[0][0].config(command=lambda row=i, col=j: click1(0, 0, 1), state=ACTIVE, activebackground="grey")
        e = e+1
    else:
        e = e+1
        for row in range(10):
            for col in range(15):
                if b1[row][col]["text"] == "🚩" and b1[row][col]["activebackground"] != "grey":
                    b1[row][col].config(text="❌")
                if b1[row][col]["activebackground"] == "grey" and b1[row][col]["state"] != DISABLED:
                     b1[row][col].config(text="💣", relief=SUNKEN, state=DISABLED, disabledforeground="red", bg="black")
        L2.config(text="😵")
        messagebox.showinfo("Result", "Ops! you clicked on a bomb!")
        x = messagebox.askquestion("Question", "Do you want to try again")
        if x == "no":
            messagebox.showinfo("Thank you", "Thank you for playing!")
            top.quit()


def flag(row, col):
    i = row
    j = col
    print(i)
    print(j)
    if b1[i][j]["state"] != DISABLED:
        global a1
        global a3
        global L3
        b1[i][j].config(text='🚩', disabledforeground="red", state=DISABLED)
        b1[i][j].bind('<Button-3>', lambda event, row=i, col=j: flag1(row, col))
        a3 = a3-1
        a1 = "🚩: {}".format(a3)
        L3.config(text=a1)


def flag1(row, col):
    i = row
    j = col
    print(i)
    print(j)
    global a1
    global a3
    global L3
    b1[i][j].config(text='', disabledforeground="red", state=NORMAL)
    b1[i][j].bind('<Button-3>', lambda event, row=i, col=j: flag(row, col))
    a3 = a3 + 1
    a1 = "🚩: {}".format(a3)
    L3.config(text=a1)


b1 = [[], [], [], [], [], [], [], [], [], []]
for i in range(10):
    for j in range(15):
        b1[i].append(button())
        b1[i][j].config(command=lambda row=i, col=j: click(row, col))
        b1[i][j].bind('<Button-3>', lambda event, row=i, col=j: flag(row, col))
        b1[i][j].grid(row=i, column=j)
e = 0
q = 0
n = ""
while n != ";":
    a = random.randrange(0, 10)
    a1 = random.randrange(0, 15)
    if b1[a][a1]["activebackground"] != "grey" and b1[a][a1] != b1[0][0]:
        b1[a][a1].config(command=lambda row=a, col=a1: click1(row, col, e), state=ACTIVE, activebackground="grey")
        q = q+1
        o.append(q)
        o1.append(b1[a][a1])
        if q == 40:
            break
        else:
            continue
    else:
       continue
min = 00
sec = 00
b = "{}:{}".format(min, sec)
lbl = Label(top, text=b,  font=("calibri", 20, "bold"), foreground="black", width=7)
lbl.grid(row=15, column=12, columnspan=3)
L1 = Label(top, text="Time: ", font="bold")
L = Label(text="MineSweeper", font="bold")
L2 = Label(text="😃", font="bold")
a3 = 40
a1 = "🚩: {}".format(a3)
L3 = Label(text=a1, font="bold")
L.grid(row=15, column=6, columnspan=3)
L1.grid(row=15, column=10, columnspan=3)
L2.grid(row=15, column=0, columnspan=3)
L3.grid(row=15, column=3, columnspan=3)
top.resizable(height=False, width=False)
messagebox.showwarning("Warning", "The mines have been placed be careful at every move ")
time()
top.mainloop()