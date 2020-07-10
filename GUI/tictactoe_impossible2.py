from tkinter import Tk, Button
from copy import deepcopy
from tkinter import messagebox


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
        self.app.title('Tic Tac Toe')
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

    def reset(self):
        self.board = Board()
        self.update()

    def exit(self):
        messagebox.showinfo("Thank You", "Thank you for playing")
        self.app.quit()

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


if __name__ == '__main__':
    GUI().mainloop()