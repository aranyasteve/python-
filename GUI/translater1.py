from tkinter import *
from googletrans import Translator


class converter():
    trans = Translator()
    top = Tk()
    a3 = None
    b3 = None
    t = None
    t3 = None

    def translator(self):
        global a3
        global b3
        global t
        t1 = a.get()
        t = self.trans.translate(t1)
        self.L1.config(text=f'Identified Language: {t.src}')
        self.L2.config(text=f'en:  {t.text}')
        self.b1.config(state=NORMAL, command=self.translater1)
        a3 = t.text
        b3 = t.src

    def translater1(self):
        self.b.config(command=self.translate2)
        self.b1.config(state=DISABLED)
        self.L1.config(text="Enter en")
        self.L2.config(text='')

    def translate3(self):
        global a3
        self.b.config(command=self.translate4)
        self.b1.config(state=DISABLED)
        self.L1.config(text=f"Enter {b3}")
        self.L2.config(text='')

    def translate2(self):
        global a3
        global b3
        global t
        global t3
        t1 = self.a.get()
        t3 = self.trans.translate(t1, src='en', dest=f'{t.src}')
        self.L1.config(text='Enter en: ')
        self.L2.config(text=f'{t.src}:  {t3.text}')
        self.b1.config(state=NORMAL, command=self.translate3)
        a3 = t3.text
        b3 = t.src

    def translate4(self):
        global a3
        global b3
        global t
        global t3
        t1 = self.a.get()
        t3 = self.trans.translate(t1, src=f'{b3}', dest='en')
        self.L1.config(text=f'Enter {b3}')
        self.L2.config(text=f'en:  {t3.text}')
        self.b1.config(state=NORMAL, command=self.translater1)
        a3 = t3.text
        b3 = t3.src
        t3 = None

    def mainloop(self):
        self.start()
        self.top.mainloop()

    def start(self):
        self.top.minsize(400, 390)
        self.top.resizable(height=False, width=False)
        self.top.title("Translator")
        L = Label(self.top, text="Translator", font=40)
        L1 = Label(self.top, text="Enter text", font=40)
        a = Entry(self.top, font=40)
        L2 = Label(self.top, text="", font=40)
        b = Button(self.top, text="Translate", width=30, height=1, relief=SUNKEN, bg="white", command=self.translator, font=40)
        b2 = Button(self.top, text="Reset", width=30, height=1, relief=SUNKEN, bg="white", font=40)
        b1 = Button(text="↕", state=DISABLED, font=20)
        L.place(x=150, y=0)
        a.place(x=200, y=50, width=170, height=120)
        L1.place(x=10, y=100)
        L2.place(x=80, y=210)
        b.place(x=50, y=310)
        b1.place(x=30, y=210)
        b2.place(x=50, y=350)


if __name__ == "__main__":
    a = converter()
    converter.mainloop(a)

