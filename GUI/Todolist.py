from tkinter import *

o = []


def todo():
    v = 10
    w = 10
    top = Tk()
    top.title("To Do List")
    top.configure(background="grey")
    top.minsize(300, 650)
    top.resizable(height=False, width=300)
    global o
    L = Label(text="Todo List", font="bold", fg="black")
    L.place(x=90, y=w)
    for j in o:
        C = Checkbutton(text=j, bg="white", fg="grey", pady=10, padx=10, width=20, font="bold", activebackground="black",
                        activeforeground="white", justify=RIGHT)
        w = w+60
        C.place(x=v, y=w)
    top.mainloop()


print("Hi there! I am Aranya at your service. I will make your todo list for the day!\nSo let's get started.")
a = int(input("How many tasks you want to create?"))
if a > 10:
    print("Sorry can only make till 7")
    exit(0)
print("Ok")
for i in range(a):
    b = input(f"Enter your work for task {i+1}")
    o.append(b)
print("Creating your todo list.......")
print("Your todo list is created check it out!")
todo()







