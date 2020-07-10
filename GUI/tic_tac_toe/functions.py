from tkinter import *
from tkinter import messagebox
from copy import deepcopy

# 1_Player(Hard)


def hard():
    class Board:

        def __init__(self, other=None):
            self.player = 'X'
            self.opponent = 'O'
            self.empty = ''
            self.size = 3
            self.fields = {}
            for y in range(self.size):
                for x in range(self.size):
                    self.fields[x, y] = self.empty
            # copy constructor
            if other:
                self.__dict__ = deepcopy(other.__dict__)

        def move(self, x, y):
            board = Board(self)
            board.fields[x, y] = board.player
            (board.player, board.opponent) = (board.opponent, board.player)
            return board

        def __minimax(self, player):
            if self.won():
                if player:
                    return (-1, None)
                else:
                    return (+1, None)
            elif self.tied():
                return (0, None)
            elif player:
                best = (-2, None)
                for x, y in self.fields:
                    if self.fields[x, y] == self.empty:
                        value = self.move(x, y).__minimax(not player)[0]
                        if value > best[0]:
                            best = (value, (x, y))
                return best
            else:
                best = (+2, None)
                for x, y in self.fields:
                    if self.fields[x, y] == self.empty:
                        value = self.move(x, y).__minimax(not player)[0]
                        if value < best[0]:
                            best = (value, (x, y))
                return best

        def best(self):
            return self.__minimax(True)[1]

        def tied(self):
            for (x, y) in self.fields:
                if self.fields[x, y] == self.empty:
                    return False
            return True

        def won(self):
            # horizontal
            for y in range(self.size):
                winning = []
                for x in range(self.size):
                    if self.fields[x, y] == self.opponent:
                        winning.append((x, y))
                if len(winning) == self.size:
                    return winning
            # vertical
            for x in range(self.size):
                winning = []
                for y in range(self.size):
                    if self.fields[x, y] == self.opponent:
                        winning.append((x, y))
                if len(winning) == self.size:
                    return winning
            # diagonal
            winning = []
            for y in range(self.size):
                x = y
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
            # other diagonal
            winning = []
            for y in range(self.size):
                x = self.size - 1 - y
                if self.fields[x, y] == self.opponent:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
            # default
            return None

        def __str__(self):
            string = ''
            for y in range(self.size):
                for x in range(self.size):
                    string = string + self.fields[x, y]
                string += "\n"
            return string

    class GUI:

        def __init__(self):
            self.app = Tk()
            self.app.title('Tic Tac Toe (Hard)')
            self.menubar = Menu(self.app)
            self.filemenu=Menu(self.menubar, tearoff=0)
            menubar = Menu(self.app)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Select a mode", state=DISABLED)
            filemenu.add_command(label="Normal", command=self.eas)
            filemenu.add_command(label="1v1", command=self.pl)

            filemenu.add_separator()

            filemenu.add_command(label="Exit", command=self.exit)
            menubar.add_cascade(label="Menu", menu=filemenu)
            self.app.config(menu=menubar)
            self.app.resizable(width=False, height=False)
            self.board = Board()
            # self.font = Font(family="Helvetica", size=32)
            self.buttons = {}
            # print(self.board.fields)
            for x, y in self.board.fields:
                handler = lambda x=x, y=y: self.move(x, y)
                button = Button(self.app,  command=handler, padx=1, bg="light blue", width=3, text="  ",
                                font=("arial", 60, "bold"), relief="sunken", border=10)
                button.grid(row=y, column=x)
                self.buttons[x, y] = button
            handler = lambda: self.reset()
            handler1 = lambda: self.exit()
            button = Button(self.app, text='RESET', font="bold", command=handler)
            button1 = Button(self.app, text="EXIT", font="bold", command=handler1)
            button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")
            button1.grid(row=self.board.size + 2, column=0, columnspan=self.board.size, sticky="WE")
            self.update()

        def eas(self):
            self.app.destroy()
            easy()

        def pl(self):
            self.app.destroy()
            ply()

        def reset(self):
            self.board = Board()
            self.update()

        def exit(self):
            messagebox.showinfo("Thank You", "Thank you for playing")
            self.app.destroy()
            exit(0)
            # self.app.quit()

        def check(self):
            if self.buttons[0, 0]["state"] == self.buttons[0, 1]["state"] == self.buttons[0, 2]["state"] == self.buttons[1, 0]["state"] == self.buttons[1, 1]["state"] == self.buttons[1, 2]["state"] == self.buttons[2, 0]["state"] == self.buttons[2, 1]["state"] == self.buttons[2, 2]["state"] == "disabled":
                for x in range(3):
                    for y in range(3):
                        self.buttons[x, y].config(disabledforeground="red")
                messagebox.showinfo("Result", "It is a draw! \nPress reset to try again")


        def move(self, x, y):
            self.app.config(cursor="watch")
            self.app.update()
            self.board = self.board.move(x, y)
            self.update()
            move = self.board.best()
            if move:
                self.board = self.board.move(*move)
                self.update()
            self.app.config(cursor="")

        def update(self):
            for (x, y) in self.board.fields:
                text = self.board.fields[x, y]
                self.buttons[x, y]['text'] = text
                self.buttons[x, y]['disabledforeground'] = 'black'
                if text == self.board.empty:
                    self.buttons[x, y]['state'] = 'normal'
                else:
                    self.buttons[x, y]['state'] = 'disabled'
            winning = self.board.won()
            if winning:
                for x, y in winning:
                    self.buttons[x, y]['disabledforeground'] = 'red'
                messagebox.showinfo("Result", "Computer has won")
                x = messagebox.askquestion("Question", "Do you want to try again?")
                if x == "no":
                    self.exit()
                self.reset()

            for (x, y) in self.board.fields:
                self.buttons[x, y].update()
            else:
                self.check()


        def mainloop(self):
            self.app.mainloop()

    GUI().mainloop()


# 1_Player(Normal)


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
            if v == "no":
                exitt()
            reseet()

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
        # root.quit()
        root.destroy()
        exit(0)

    def reseet():
        root.destroy()
        # root.quit()
        easy()

    def two_player():
        root.destroy()
        ply()

    def hard1():
        root.destroy()
        hard()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Select a mode", state=DISABLED)
    filemenu.add_command(label="1v1", command=two_player)
    filemenu.add_command(label="Hard", command=hard1)

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


# 1v1


def ply():

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
            v = messagebox.askquestion("Question", "Do you want to try again?")
            if v == "no":
                exxit()
            reset()
        elif b[0][0]["text"] == b[0][1]["text"] == b[0][2]["text"] == "  O  " or \
             b[0][0]["text"] == b[1][0]["text"] == b[2][0]["text"] == "  O  " or \
             b[0][2]["text"] == b[1][2]["text"] == b[2][2]["text"] == "  O  " or \
             b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == "  O  " or \
             b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == "  O  " or \
             b[2][0]["text"] == b[2][1]["text"] == b[2][2]["text"] == "  O  " or \
             b[1][0]["text"] == b[1][1]["text"] == b[1][2]["text"] == "  O  " or \
             b[0][1]["text"] == b[1][1]["text"] == b[2][1]["text"] == "  O  ":
            messagebox.showinfo("Congrats", "O has won!")
            v = messagebox.askquestion("Question", "Do you want to try again?")
            if v == "no":
                exxit()
            reset()
        elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] ==   \
             b[1][0]["state"] == b[1][1]["state"] == b[1][2]["state"] ==   \
             b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"]:
            messagebox.showinfo("Draw", "Draw!,No one has won...")
            v = messagebox.askquestion("Question", "Do you want to try again?")
            if v == "no":
                exxit()
            reset()

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

    def hard1():
        top.destroy()
        hard()

    def easy1():
        top.destroy()
        easy()

    def exxit():
        messagebox.showinfo("Thank you", "Thank you for playing")
        # top.quit()
        top.destroy()
        exit(0)

    def reset():
        top.destroy()
        # top.quit()
        ply()

    top = Tk()
    top.title("Tic Tac Toe (1v1)")
    menubar = Menu(top)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Select a mode", state=DISABLED)
    filemenu.add_command(label="Normal", command=easy1)
    filemenu.add_command(label="Hard", command=hard1)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=exxit)
    menubar.add_cascade(label="Menu", menu=filemenu)
    top.config(menu=menubar)

    b = [[], [], []]
    for i in range(3):
        for j in range(3):
            b[i].append(button())
            b[i][j].config(command=lambda row=i, col=j: click(row, col))
            b[i][j].grid(row=i, column=j)
    L = Label(top, text="X's chance", font=("ariel", 30, "bold"))
    L1 = Button(top, text="EXIT", command=exxit, font="bold")
    L2 = Button(top, text="RESET", command=reset, font="bold")
    L.grid(row=3, column=0, columnspan=3)
    L1.grid(row=5, column=0, columnspan=3, sticky="WE")
    L2.grid(row=4, column=0, columnspan=3, sticky="WE")
    top.resizable(height=False, width=False)
    top.mainloop()