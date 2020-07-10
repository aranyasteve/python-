from tkinter import *
from tkinter import messagebox
top = Tk()


def button():
    return Button(top, text="       ", pady=50, padx=50, activebackground="grey", relief="sunken",
                  font=('arial', 35, 'bold'), bg="white")


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
        top.destroy()
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
        top.destroy()
        top.quit()
    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] ==   \
         b[1][0]["state"] == b[1][1]["state"] == b[1][2]["state"] ==   \
         b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"]:
        messagebox.showinfo("Draw", "Draw!,No one has won...")
        top.destroy()
        top.quit()


def click(row, col):
        b[row][col].config(text="  X  ", state=DISABLED, disabledforeground="Red")
        check()
        click1()


def click1():
    if b[1][1]["state"] == NORMAL:
        b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][1]["text"] == b[2][0]['text'] == "  X  ":
        b[0][3].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[1][1]["text"] == "  X  ":
        b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][2]["text"] == b[1][1]["text"] == "  X  ":
        b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[2][2]["text"] == "  X  ":
        b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[0][1]["text"] == "  X  ":
        b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[0][2]["text"] == "  X  ":
        b[0][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][1]["text"] == b[0][2]["text"] == "  X  ":
        b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[1][0]["text"] == "  X  ":
        b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][0]["text"] == b[1][0]["text"] == "  X  ":
        b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[2][0]["text"] == "  X  ":
        b[1][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][2]["text"] == b[1][1]["text"] == "  X  ":
        b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][0]["text"] == b[1][1]["text"] == "  X  ":
        b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][2]["text"] == b[2][0]["text"] == "  X  ":
        b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][1]["text"] == b[1][1]["text"] == "  X  ":
        b[2][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][1]["text"] == b[2][1]["text"] == "  X  ":
        b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][1]["text"] == b[1][1]["text"] == "  X  ":
        b[0][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[1][0]["text"] == b[1][1]["text"] == "  X  ":
        b[1][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[1][1]["text"] == b[1][2]["text"] == "  X  ":
        b[1][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[1][0]["text"] == b[1][2]["text"] == "  X  ":
        b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[1][2]["text"] == b[2][2]["text"] == "  X  ":
        b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][2]["text"] == b[0][2]["text"] == "  X  ":
        b[1][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[1][2]["text"] == b[0][2]["text"] == "  X  ":
        b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][0]["text"] == b[2][1]["text"] == "  X  ":
        b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][2]["text"] == b[2][1]["text"] == "  X  ":
        b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[2][0]["text"] == b[2][2]["text"] == "  X  ":
        b[2][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
        check()
    elif b[0][0]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][2]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[2][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[0][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[0][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][1]["text"] == b[0][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[1][0]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][0]["text"] == b[1][0]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][0]["text"] == b[2][0]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][2]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][0]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][2]["text"] == b[2][0]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][1]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[0][1]["text"] == b[2][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][1]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][0]["text"] == b[1][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][1]["text"] == b[1][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][0]["text"] == b[1][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][2]["text"] == b[2][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[0][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][2]["text"] == b[0][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[1][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][2]["text"] == b[0][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][0]["text"] == b[2][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][2].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][2]["text"] == b[2][1]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][0].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[2][0]["text"] == b[2][2]["text"] == "  O  ":
        if b[2][2]["text"] != "  X  ":
            b[2][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    elif b[1][0]["text"] == b[1][2]["text"] == "  X  " and b[1][1]["text"] == "  O  ":
        b[2][1].config(text="  O  ", state=DISABLED, disabledforeground="blue")
    else:
        t = []
        for row in range(3):
            for col in range(3):
                if b[row][col]["state"] == NORMAL:
                    t.append(b[i][j])
                    a = t[0]
                    a.config(text="  O  ", state=DISABLED, disabledforeground="blue")
                    check()


top.title("Tic Tac Toe")
b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button())
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)
L = Label(top, text="Tic Tac Toe", font=("ariel", 30, "bold"))
L.grid(row=3, column=0, columnspan=3)
top.mainloop()
