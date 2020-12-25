from tkinter import *
from googletrans import Translator

trans = Translator()
top = Tk()
img = PhotoImage(file="t.png")
top.iconphoto(False, img)
photo = img.subsample(17, 17)
a3 = None
b3 = None
t = None
t3 = None


def start():

        def translator():
            global a3
            global b3
            global t
            t1 = a.get()
            t = trans.translate(t1)
            L1.config(text="")
            L2.config(text="")
            L1.config(text=f'Identified Language: {t.src}')
            L2.config(text=f'en:  {t.text}')
            b1.config(state=NORMAL, command=translator1)
            a3 = t.text
            b3 = t.src

        def translator1():
            b.config(command=translate2)
            b1.config(state=DISABLED)
            L1.config(text="")
            L2.config(text="")
            L1.config(text="Enter en")
            L2.config(text='')

        def translate2():
            global a3
            global b3
            global t
            global t3
            t1 = a.get()
            t3 = trans.translate(t1, src='en', dest=f'{t.src}')
            L1.config(text="")
            L2.config(text="")
            L1.config(text='en: ')
            L2.config(text=f'{t.src}:  {t3.text}')
            b1.config(state=NORMAL, command=translate3)
            a3 = t3.text
            b3 = t.src

        def translate3():
            global a3
            b.config(command=translate4)
            b1.config(state=DISABLED)
            L1.config(text="")
            L2.config(text="")
            L1.config(text=f"Enter {b3}")
            L2.config(text='')

        def translate4():
            global a3
            global b3
            global t
            global t3
            t1 = a.get()
            t3 = trans.translate(t1, src=f'{b3}', dest='en')
            L1.config(text="")
            L2.config(text="")
            L1.config(text=f'{b3}: ')
            L2.config(text=f'en:  {t3.text}')
            b1.config(state=NORMAL, command=translator1)
            a3 = t3.text
            b3 = t3.src
            t3 = None

        def reset():
            top.quit()
            L1.config(text="")
            L2.config(text="")
            start()

        top.minsize(450, 400)
        top.resizable(height=False, width=False)
        top.title("Translator")
        L = Label(top, text="Translator", font=5)
        L1 = Label(top, text="Enter text: ", font=5)
        a = Entry(top, font=5)
        L2 = Label(top, text="", font=5)
        b = Button(top, text="Translate", width=30, height=1, relief=SUNKEN, bg="white", command=translator, font=5)
        b2 = Button(top, text="Reset", width=30, height=1, relief=SUNKEN, bg="white",  command=reset,
                    font=40)
        b1 = Button(text="↕", state=DISABLED, font=20)
        L.place(x=170, y=0)
        a.place(x=250, y=90, width=195, height=65)
        L1.place(x=10, y=110)
        L2.place(x=80, y=210)
        b.place(x=50, y=310)
        b1.place(x=30, y=210)
        b2.place(x=50, y=350)
        top.mainloop()


start()
