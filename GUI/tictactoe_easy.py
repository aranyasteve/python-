from tkinter import *
from tkinter import messagebox
import random

top = Tk()


def button():
    return Button(top, padx=1, bg="light blue", width=3, text="  ",
                  font=("arial", 60, "bold"), relief="sunken", border=10)


def check():
    if b[0][0]["text"] == b[0][1]["text"] == b[0][2]["text"] == "  X  " or \
       b[0][0]["text"] == b[1][0]["text"] == b[2][0]["text"] == "  X  " or \
       b[0][2]["text"] == b[1][2]["text"] == b[2][2]["text"] == "  X  " or \
       b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == "  X  " or \
       b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == "  X  " or \
       b[2][0]["text"] == b[2][1]["text"] == b[2][2]["text"] == "  X  " or \
       b[1][0]["text"] == b[1][1]["text"] == b[1][2]["text"] == "  X  " or \
       b[0][1]["text"] == b[1][1]["text"] == b[2][1]["text"] == "  X  ":
        messagebox.showinfo("Congrats", "X has won!")
        top.quit()
    elif b[0][0]["text"] == b[0][1]["text"] == b[0][2]["text"] == "  O  " or \
         b[0][0]["text"] == b[1][0]["text"] == b[2][0]["text"] == "  O  " or \
         b[0][2]["text"] == b[1][2]["text"] == b[2][2]["text"] == "  O  " or \
         b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == "  O  " or \
         b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == "  O  " or \
         b[2][0]["text"] == b[2][1]["text"] == b[2][2]["text"] == "  O  " or \
         b[1][0]["text"] == b[1][1]["text"] == b[1][2]["text"] == "  O  " or \
         b[0][1]["text"] == b[1][1]["text"] == b[2][1]["text"] == "  O  ":
        messagebox.showinfo("Congrats", "O has won!")
        top.quit()
    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] ==   \
         b[1][0]["state"] == b[1][1]["state"] == b[1][2]["state"] ==   \
         b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"]:
        messagebox.showinfo("Draw", "Draw!,No one has won...")
        top.quit()


def click(row,col):
    b[row][col].config(text="X", state=DISABLED, disabledforeground="Red")
    check()
    row, col = click1()
    b[row][col].config(text="O", state=DISABLED, disabledforeground="blue")
    check()


def click1():
    t = []
    for row in range(3):
        for col in range(3):
            if b[row][col]["state"] != DISABLED:
                t.append(b[row][col])
                return random.choice(t)




b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button())
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(column=i, row=j)
top.mainloop()