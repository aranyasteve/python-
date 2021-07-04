from tkinter import *
import pyttsx3
engine = pyttsx3.init()


class speech():
    def __init__(self):
        self.top = Tk()
        # self.img = PhotoImage(file="g.png")
        # self.top.iconphoto(False, self.img)
        # self.photo = self.img.subsample(17, 17)
        self.top.minsize(300, 200)
        self.top.resizable(height=False, width=False)
        self.top.title("Text Recognition")
        self.L = Label(self.top, text="Text to Voice")
        self.L1 = Label(self.top, text="Text")
        self.a = Entry(self.top)
        self.b = Button(self.top, text="Speak", width=30, height=1, relief=SUNKEN, bg="white", command=self.click)
        self.L.place(x=100, y=0)
        self.a.place(x=120, y=50)
        self.L1.place(x=50, y=50)
        self.b.place(x=43, y=170)

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def click(self):
        if engine.isBusy():
            a = ''
        else:
            text = self.a.get()
            self.speak(text)

    def mainloop(self):
        self.top.mainloop()
        engine.say("Hi, Welcome to text to speech recognition! I will read whatever you enter in the entry box. I am "
                   "useful in many purposes you can learn how to pronounce words by making me spell the word or you"
                   " can tell" 
                   "me what to read if you are not able to read it."
                   "so what are you waiting for start typing! ")
        engine.runAndWait()


if __name__ == "__main__":
    speech().mainloop()