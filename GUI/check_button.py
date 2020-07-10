from tkinter import *
from tkinter import messagebox
top = Tk()


def command():
    messagebox.showinfo("file", "Well Done!")


def command2():
    messagebox.showinfo("file", "Good Night!")


C1 = Checkbutton(top, text="Get up", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green",
                 offvalue=1, onvalue=1)
C2 = Checkbutton(top, text="Brush and Have Bath", bg="red", fg="blue", activebackground="black", activeforeground="grey"
                 , font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C3 = Checkbutton(top, text="Eat Breakfast", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C4 = Checkbutton(top, text="Study", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C5 = Checkbutton(top, text="Have lunch", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C6 = Checkbutton(top, text="Rest", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C7 = Checkbutton(top, text="Play any sport", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C8 = Checkbutton(top, text="Have snacks", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C9 = Checkbutton(top, text="Study", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                 font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C10 = Checkbutton(top, text="Have Dinner", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                  font="bold", cursor="mouse", command=command, pady=5, padx=5, state=ACTIVE, selectcolor="green")
C11 = Checkbutton(top, text="Sleep", bg="red", fg="blue", activebackground="black", activeforeground="grey",
                  font="bold", cursor="mouse", command=command2, pady=5, padx=5, state=ACTIVE, selectcolor="green", onvalue=0)

C1.place(x=10, y=10)
C2.place(x=10, y=70)
C3.place(x=10, y=130)
C4.place(x=10, y=190)
C5.place(x=10, y=250)
C6.place(x=10, y=310)
C7.place(x=10, y=370)
C8.place(x=10, y=430)
C9.place(x=10, y=490)
C10.place(x=10, y=550)
C11.place(x=10, y=620)
# a = False
# if C1.select():
#     a = True
#     print(a)
top.mainloop()
