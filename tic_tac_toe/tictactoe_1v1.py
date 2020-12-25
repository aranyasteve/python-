from tkinter import *
from tkinter import messagebox
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


def click(row, col):
    b[row][col].config(text="  X  ", state=DISABLED, disabledforeground="Red")
    L.config(text="O's chance")

    check()
    for i in range(3):
        for j in range(3):
            b[i][j].config(command=lambda row=i, col=j: click1(row, col))


def click1(row, col):
    b[row][col].config(text="  O  ", state=DISABLED, disabledforeground="Blue")
    L.config(text="X's chance")
    check()
    for i in range(3):
        for j in range(3):
            b[i][j].config(command=lambda row=i, col=j: click(row, col))


def exxit():
    messagebox.showinfo("Thank you", "Thank you for playing")
    top.quit()


top.title("Tic Tac Toe")
b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button())
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)
L = Label(top, text="X's chance", font=("ariel", 30, "bold"))
L1 = Button(top, text="EXIT", command=exxit, font="bold")
L2 = Button(top, text="RESET", command=exxit, font="bold")
L.grid(row=3, column=0, columnspan=3)
L1.grid(row=4, column=0, columnspan=3, sticky="WE")
L2.grid(row=5, column=0, columnspan=3, sticky="WE")
top.resizable(height=False, width=False)

top.mainloop()

