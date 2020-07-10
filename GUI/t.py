from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM,fill=BOTH)

mylist = Listbox(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar1.set)
for line in range(100):
   mylist.insert(END, "This is line numberr " + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
scrollbar1.config(command=mylist.xview)

mainloop()