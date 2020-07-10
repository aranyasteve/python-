from tkinter import *
from tkinter import messagebox

def easy():
    root = Tk()
    root.title("Tic Tac Toe (Normal)")

    def button():
        return Button(root, padx=1, bg="light blue", width=3, text="  ",
                      font=("arial", 60, "bold"), relief="sunken", border=10)

    def check():
        if b[0][0]["text"] == b[0][1]["text"] == b[0][2]["text"] == "X" or \
                b[0][0]["text"] == b[1][0]["text"] == b[2][0]["text"] == "X" or \
                b[0][2]["text"] == b[1][2]["text"] == b[2][2]["text"] == "X" or \
                b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == "X" or \
                b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == "X" or \
                b[2][0]["text"] == b[2][1]["text"] == b[2][2]["text"] == "X" or \
                b[1][0]["text"] == b[1][1]["text"] == b[1][2]["text"] == "X" or \
                b[0][1]["text"] == b[1][1]["text"] == b[2][1]["text"] == "X":
            messagebox.showinfo("Result", "You have won!")
            x = messagebox.askquestion("Question", "Do you want to try again")
            if x == "no":
                exitt()
            reseet()
        elif b[0][0]["text"] == b[0][1]["text"] == b[0][2]["text"] == "O" or \
                b[0][0]["text"] == b[1][0]["text"] == b[2][0]["text"] == "O" or \
                b[0][2]["text"] == b[1][2]["text"] == b[2][2]["text"] == "O" or \
                b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == "O" or \
                b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == "O" or \
                b[2][0]["text"] == b[2][1]["text"] == b[2][2]["text"] == "O" or \
                b[1][0]["text"] == b[1][1]["text"] == b[1][2]["text"] == "O" or \
                b[0][1]["text"] == b[1][1]["text"] == b[2][1]["text"] == "O":
            messagebox.showinfo("Result", "Computer has won!")
            x = messagebox.askquestion("Question", "Do you want to try again")
            if x == "no":
                exitt()
            reseet()
        elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == \
                b[1][0]["state"] == b[1][1]["state"] == b[1][2]["state"] == \
                b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"]:
            messagebox.showinfo("Draw", "Draw!, No one has won...")
            v = messagebox.askquestion("Question", "Do you want to try again?")
            if v == "yes":
                reseet()
            exitt()

    def click(row, col):
        b[row][col].config(text="X", state=DISABLED, disabledforeground="Red")
        check()
        click1()

    def click1():
        t = []
        for row in range(3):
            for col in range(3):
                if b[row][col]["state"] != DISABLED:
                    t.append(b[row][col])
        a = t[0]
        a.config(text="O", state=DISABLED, disabledforeground="blue")
        check()

    def exitt():
        messagebox.showinfo("Thank you", "Thank you for Playing")
        root.quit()
        root.destroy()

    def reseet():
        root.destroy()
        root.quit()

    def plyy():
        root.destroy()

    def hardd():
        root.destroy()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Select a mode", state=DISABLED)
    filemenu.add_command(label="2v2", command=plyy)
    filemenu.add_command(label="1v1(Hard)", command=hardd)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=exitt)
    menubar.add_cascade(label="Menu", menu=filemenu)
    root.config(menu=menubar)

    b = [[], [], []]
    for i in range(3):
        for j in range(3):
            b[i].append(button())
            b[i][j].config(command=lambda row=i, col=j: click(row, col))
            b[i][j].grid(column=i, row=j)
            button1 = Button(root, text='RESET', font="bold", command=reseet)
            button2 = Button(root, text="EXIT", font="bold", command=exitt)
            button1.grid(row=4, column=0, columnspan=3, sticky="WE")
            button2.grid(row=5, column=0, columnspan=3, sticky="WE")

    root.resizable(height=False, width=False)
    root.mainloop()



easy()
