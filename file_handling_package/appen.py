"""
File type
1 > Plain text
2 > Binary File
Mode of plain text
w, w+
r, r+
a, a+
Mode of binary file
wb, wb+
rb, rb+
ab, ab+
"""
a = input("enter a file  you want to create")
file = open(a, "w+")
b = input("do you want to write something if yes type 'yes'else type 'no'").lower()
if b == "yes":
    c = input("enter what you want to write on your folder ")
    file.write(c)
    file.seek(0,0)
    d = input("do you want to see what you have written ? type yes or no").lower()
    if d == "yes":
        print("you have written : ", file.read())

    elif d == "no":
         print("thank you your file has been stored in python!")
    else:
        print("wrong option entered try again\n")

else:
    print("thank you for visiting python your file has been stored.")
    file.close()


