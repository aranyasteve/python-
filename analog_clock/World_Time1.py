from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageDraw, ImageTk
from math import *
import json


class Analog:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#ededed")
        self.root.geometry("700x700")
        self.root.title("World Time")
        self.root.resizable(height=False, width=False)
        self.L = Label(top, text="World Time", font=10)
        self.L.place(x=320, y=0)
        self.L1 = Label(top, text="Continent Name: ", font=5)
        self.L1.place(x=170, y=70)
        self.L2 = Label(top, text="City Name: ", font=5)
        self.L2.place(x=170, y=140)
        self.L3 = Label(text="", font=10)
        self.L3.place(x=220, y=210)
        self.B = Button(top, text="Check", font=10, relief=SUNKEN, width=30, bg="#dedede", command=self.get_time)
        self.B.place(x=210, y=650)
        self.E = Entry(top, font=('Courier', 15))
        self.E.place(x=320, y=70, height=30, width=200)
        self.E1 = Entry(top, font=('Courier', 15))
        self.E1.place(x=320, y=140, height=30, width=200)
        self.lbl = Label(self.root, bg="white", bd=10)
        self.lbl.place(x=210, y=320, height=300, width=350)
        self.image = PhotoImage(file="e.png")
        self.image.config(width=20, height=20)
        # self.get_time()

    def get_time(self):
        try:
            self.E2 = self.E.get()
            self.E3 = self.E1.get()
            url = f"http://worldtimeapi.org/api/timezone/{self.E2}/{self.E3}"
            response = requests.get(url)
            self.time = response.json()
            print(self.time)
            if self.time == {'error': 'unknown location'} and self.L3["text"] == "":
                messagebox.showerror("Error", "Please enter a valid Location")
            self.working()

        except:
            if self.lbl["text"] != "":
                messagebox.showerror("Error", "Please check you net")
            self.lbl.config(image=self.image)
            self.L3.config(text="")

    def clock_image(self, hr, min_, sec):
        clock = Image.new("RGB", (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("clock3.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        draw.line((200, 200, 200+80*sin(radians(hr)), 200-80*cos(radians(hr))), fill="black", width=5)
        draw.line((200, 200, 200+95*sin(radians(min_)), 200-95*cos(radians(min_))), fill="black", width=4)
        draw.line((200, 200, 200+100*sin(radians(sec)), 200-100*cos(radians(sec))), fill="red", width=3)

        draw.ellipse((195, 195, 210, 210), fill="black")

        clock.save("clock_new.png")
        ImageDraw.Draw(clock)

    def working(self):
        h = self.time['datetime'][11]
        h = str(h)
        h1 = self.time['datetime'][12]
        h1 = str(h1)
        h2 = h+h1
        h2 = int(h2)
        m = self.time['datetime'][14]
        m = str(m)
        m1 = self.time['datetime'][15]
        m1 = str(m1)
        m2 = m+m1
        m2 = int(m2)
        s = self.time['datetime'][17]
        s = str(s)
        s1 = self.time['datetime'][18]
        s1 = str(s1)
        s2 = s+s1
        s2 = int(s2)
        time = f"The Current Time in {self.E3} is {h2}:{m2}:{s2}"
        self.L3.config(text=time)
        hr = (h2/12)*360
        min_ = (m2/60)*360
        sec = (s2/60)*360
        self.clock_image(hr, min_, sec)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(1000, self.get_time)


top = Tk()
obj = Analog(top)
top.mainloop()