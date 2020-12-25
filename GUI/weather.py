from tkinter import *
from tkinter import messagebox
import requests
import json


def get_weather():
    try:
        E1 = E.get()
        weather_key = "92e86c74b82aca660bda96670ab555f0"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {'APPID': weather_key, 'q': E1, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()
        print(weather)
        format_response(weather)
        # description = weather['weather'][0]['description']
        # temperature = weather['main']['temp']
        # humidity = weather['main']['humidity']
        # pressure = weather['main']['pressure']
    except:
        messagebox.showerror("Error", "Please Check Your Internet Connection")


def format_response(weather):
    try:
        description = weather['weather'][0]['description']
        description = str(description)
        temperature = weather['main']['temp']
        temperature = str(temperature)
        humidity = weather['main']['humidity']
        humidity = str(humidity)
        humidity1 = humidity+" %"
        pressure = weather['main']['pressure']
        pressure = str(pressure)
        pressure1 = pressure+" mm of Hg"
        # icon = weather['weather']['icon']
        # icon = str(icon)
        L6.config(text=temperature)
        L7.config(text=pressure1)
        L8.config(text=humidity1)
        L9.config(text=description)
        # L10.config(text=icon)

    except:
        messagebox.showerror("Error", "Please Enter a Valid City Name")


top = Tk()
top.title("Weather")
top.minsize(450, 430)
top.resizable(height=False, width=False)
img = PhotoImage(file='w.png')
# img1 = PhotoImage(file='weat.gif')
top.iconphoto(False, img)
photo = img.subsample(17, 17)
L = Label(top, text="Weather App", font=10)
L.place(x=160, y=0)
L1 = Label(top, text="City Name: ", font=5)
L1.place(x=50, y=70)
L2 = Label(top, text="Temperature (°F):", font=10)
L2.place(x=10, y=150)
L6 = Label(top, text="", font=5)
L6.place(x=190, y=150)
L3 = Label(top, text="Atmospheric Pressure:", font=10)
L3.place(x=10, y=200)
L7 = Label(top, text="", font=10)
L7.place(x=230, y=200)
L4 = Label(top, text="Humidity:", font=10)
L4.place(x=10, y=250)
L8 = Label(top, text="", font=10)
L8.place(x=120, y=250)
L5 = Label(top, text="Description:", font=10)
L5.place(x=10, y=300)
L9 = Label(top, text="", font=10)
L9.place(x=150, y=300)
B = Button(top, text="Check", font=10, relief=SUNKEN, width=20, bg="white", command=get_weather)
B.place(x=110, y=390)
E = Entry(top, font=('Courier', 15))
E.place(x=200, y=70, height=30, width=200)
top.mainloop()