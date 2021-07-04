from tkinter import *
import pymysql
from tkinter import messagebox

a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()


class Read:
    def __init__(self):

        self.top = Tk()
        self.top.minsize(height=600, width=800)
        self.top.resizable(height=False, width=False)
        self.top.title("Get your Model Information")

        self.l = Label(self.top, text="Get Your Model Information", font=("bold", 19), fg="#121b6e")
        self.l.place(x=260, y=5)

        self.l7 = Label(self.top, text="Product Name: ", font=("bold", 15), fg="#121b6e")
        self.l7.place(x=170, y=70)
        self.e7 = Entry(self.top, font=("bold", 15), fg="#121b6e")
        self.e7.place(x=370, y=70)

        self.l1 = Label(self.top, text="", font=("bold", 15), fg="#121b6e")
        self.l1.place(x=90, y=210)
        self.e5 = Label(self.top, font=("bold", 15), fg="#121b6e")
        self.e5.place(x=180, y=210)

        self.l2 = Label(self.top, text="", font=("bold", 15),  fg="#121b6e")
        self.l2.place(x=500, y=210)
        self.e1 = Label(self.top, font=("bold", 15), fg="#121b6e")
        self.e1.place(x=620, y=210)

        self.l3 = Label(self.top, text="", font=("bold", 15), fg="#121b6e")
        self.l3.place(x=90, y=280)
        self.e2 = Label(self.top, font=("bold", 15), fg="#121b6e")
        self.e2.place(x=180, y=280)

        self.l4 = Label(self.top, text="", font=("bold", 15), fg="#121b6e")
        self.l4.place(x=500, y=280)
        self.e3 = Label(self.top, font=("bold", 15), fg="#121b6e")
        self.e3.place(x=620, y=280)

        self.l5 = Label(self.top, text="", font=("bold", 15), fg="#121b6e")
        self.l5.place(x=80, y=350)
        self.e4 = Label(self.top, font=("bold", 15),  fg="#121b6e")
        self.e4.place(x=180, y=350)

        self.l6 = Label(self.top, text="", font=("bold", 15), fg="#121b6e")
        self.l6.place(x=500, y=350)
        self.e6 = Label(self.top, font=("bold", 15), fg="#121b6e")
        self.e6.place(x=620, y=350)

        self.b1 = Button(self.top, text="Check", bg="white", fg="#121b6e", width=15, font=("bold", 17), command=self.submit)
        self.b1.place(x=300, y=550)

    def submit(self):
        try:
            a1 = self.e7.get()
            a1 = str(a1)
            query = f"SELECT * FROM  models  WHERE Name = '{a1}'"
            b.execute(query)
            b2 = b.fetchall()
            print(b2)
            if b2 == ():
                messagebox.showerror("Error", "Please enter a valid model")
                self.l1.config(text="")
            self.l1.config(text="Name:")
            if b2 == ():
                self.l1.config(text="")
            self.e5.config(text=f"{b2[0][1]}")

            self.l2.config(text="Company:")
            self.e1.config(text=f"{b2[0][2]}")

            self.l3.config(text="D.O.P:")
            self.e2.config(text=f"{b2[0][3]}")

            self.l4.config(text="Order_No")
            self.e3.config(text=f"{b2[0][4]}")

            self.l5.config(text="Model_No:")
            self.e4.config(text=f"{b2[0][5]}")

            self.l6.config(text="Serial_No:")
            self.e6.config(text=f"{b2[0][6]}")

            # print("Here are your details")
            # print("Name of the product ", b1[0][1])
            # print("Company Name ", b1[0][2])
            # print("Date Purchased this product ", b1[0][3])
            # print("Order Number of this product ", b1[0][4])
            # print("Model Number of this product  ", b1[0][5])
            # print("Serial Number of this product  ", b1[0][6])
            # print("Date entered this details ", b1[0][7]
            a.close()
        except Exception as e:
            a.rollback()
            messagebox.showerror("Error", "Please enter a model name you have registered")
            print(f"Sorry an error occured {e}")

    def mainloop(self):
        self.top.mainloop()


if __name__ == "__main__":
    Read().mainloop()
