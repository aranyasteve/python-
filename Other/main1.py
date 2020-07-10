from qwert.module import *

a = float(input())
opt = ''
while opt != ";":
    opt = input()
    if opt == "+":
       b = int(input())
       a = add(a,b)
    elif opt == "=":
        print(a)
    elif opt == "*":
       b = int(input())
       a = mul(a, b)
    elif opt == "/":
      b = int(input())
      a = div(a,b)
    elif opt == "-":
        b = float(input())
        a = sub(a, b)
    else:
        h=input("syntax error....\nenter any key to continue\nand No for exit.").upper()
        if h == 'NO':
            opt = ';'