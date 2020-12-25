from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from datetime import datetime
import time
from math import *


class Analog:
    def __init__(self, root):
        self.root = root
        # self.image = PhotoImage(file="earth.jpg")
        # self.root.iconphoto(False, self.image)
        # photo = self.image.subsample(17, 17)
        self.root.title("Analog Clock")
        self.root.geometry("450x570")
        self.root.resizable(height=False, width=False)
        self.root.config(bg="#021e2f")
        title = Label(self.root, text="Analog Clock", font=("times new roman", 50, "bold"), bg="#04444a", fg="white").place(x=0, y=50, relwidth=1)
        self.lbl = Label(self.root, bg="grey", bd=20, relief=RAISED)
        self.lbl.place(x=25, y=150, height=400, width=400)
        # self.clock_image()
        self.working()

    def clock_image(self, hr, min_, sec):
        clock = Image.new("RGB", (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)

        # Clock image is  made
        bg = Image.open("clock3.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))

        # Hour Line
        draw.line((200, 200, 200+80*sin(radians(hr)), 200-80*cos(radians(hr))), fill="black", width=5)

        # Minute Line
        draw.line((200, 200, 200+95*sin(radians(min_)), 200-95*cos(radians(min_))), fill="black", width=4)

        # Seconds Line
        draw.line((200, 200, 200+100*sin(radians(sec)), 200-100*cos(radians(sec))), fill="red", width=3)

        draw.ellipse((195, 195, 210, 210), fill="black")

        # Saving the Image
        clock.save("clock_new.png")
        ImageDraw.Draw(clock)

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        # print(h, m, s)
        hr = (h/12)*360
        min_ = (m/60)*360
        sec = (s/60)*360
        self.clock_image(hr, min_, sec)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)





top = Tk()
obj = Analog(top)
top.mainloop()
