from tkinter import *
import pymysql
from tkinter import messagebox

a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()


class Create():
    def __init__(self):
        self.top = Tk()
        self.top.minsize(height=400, width=900)
        self.top.resizable(height=False, width=False)
        self.top.title("Register your Model")

        self.l = Label(self.top, text="Register Your Information", font=("bold", 19),  fg="#121b6e")
        self.l.place(x=320, y=0)

        self.l1 = Label(self.top, text="Name:", font=("bold", 15),  fg="#121b6e")
        self.l1.place(x=90, y=70)
        self.e5 = Entry(self.top, font=("bold", 15),  fg="#121b6e")
        self.e5.place(x=180, y=70)

        self.l2 = Label(self.top, text="Company:", font=("bold", 15),  fg="#121b6e")
        self.l2.place(x=500, y=70)
        self.e1 = Entry(self.top, font=("bold", 15), fg="#121b6e")
        self.e1.place(x=620, y=70)

        self.l3 = Label(self.top, text="D.O.P:", font=("bold", 15),  fg="#121b6e")
        self.l3.place(x=90, y=140)
        self.e2 = Entry(self.top, font=("bold", 15),  fg="#121b6e")
        self.e2.place(x=180, y=140)

        self.l4 = Label(self.top, text="Model_No:", font=("bold", 15),  fg="#121b6e")
        self.l4.place(x=500, y=140)
        self.e3 = Entry(self.top, font=("bold", 15),  fg="#121b6e")
        self.e3.place(x=620, y=140)

        self.l5 = Label(self.top, text="Serial_No:", font=("bold", 15),  fg="#121b6e")
        self.l5.place(x=80, y=210)
        self.e4 = Entry(self.top, font=("bold", 15),  fg="#121b6e")
        self.e4.place(x=180, y=210)

        self.l5 = Label(self.top, text="Order_No:", font=("bold", 15),  fg="#121b6e")
        self.l5.place(x=500, y=210)
        self.e6 = Entry(self.top, font=("bold", 15),  fg="#121b6e")
        self.e6.place(x=620, y=210)

        self.b1 = Button(self.top, text="Submit", bg="white", fg="#121b6e", width=15, font=("bold", 17), command=self.submit)
        self.b1.place(x=340, y=340)

    def submit(self):
        d1 = self.e5.get()
        d2 = self.e1.get()
        d3 = self.e2.get()
        d4 = self.e3.get()
        d5 = self.e4.get()
        d6 = self.e6.get()

        try:
            query = """INSERT INTO models (Name, Company, D_O_P, Order_No, Model_No, Serial_No)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(d1, d2, d3, d6, d4, d5)
            b.execute(query)
            messagebox.showinfo("Conformed", "Your Details are registered")
            self.top.destroy()
            a.commit()
            a.close()
            # exit(0)
        except Exception as e:
            a.rollback()
            print(f"Sorry an error occured {e}")

    def mainloop(self):
        self.top.mainloop()


if __name__ == "__main__":
    Create().mainloop()