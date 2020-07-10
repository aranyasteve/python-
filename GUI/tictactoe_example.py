from tkinter import *
from tkinter import messagebox
import random as r


def button(top):
    b = Button(top, padx=1, bg="white", width=3, text="     ",
               font=('arial', 60, 'bold'), relief="sunken", bd=10)
    return b


def check():  # Checks for victory or Draw
    for i in range(3):
        if(b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] ==
                b[1][i]["text"] == b[2][i]["text"] == a):
            messagebox.showinfo("Congrats!!", "'" + a + "' has won")

    if(b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or
            b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == a):
        messagebox.showinfo("Congrats!!", "'"+a+"' has won")

    elif(b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] ==
         b[1][1]["state"] == b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] ==
         b[2][2]["state"] == DISABLED):
        messagebox.showinfo("Tied!!", "The match ended in a draw")


def click(row, col):
    b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
    check()
    # label.config(text=a + "'s Chance")

######################### Game Start #########################


windows = Tk()
windows.title('Tic Tac Toe')
a = r.choice(['O', 'X'])
colour = {'O': 'blue', 'X': 'red'}

b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button(windows))
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)
lable = Label(text=a+"'s Chance", font=('arial', 20, 'bold'))
lable.grid(row=3, column=0, columnspan=3)


windows.mainloop()


