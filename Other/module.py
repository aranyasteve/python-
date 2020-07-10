from Other.python_module import *
import random

random.random()

name = input("hello,to continue please introduce your name.")
print("NOTE:this python process is indefinite..")
l=''
while l != ";":
 l = input("enter a symbol, + for addition , - for subtraction,* for multiplication, / for division if you want to exit the process type ; ")
 if l == "+":
    print(add())
 elif l == "-":
  print(sub())
 elif l == "*":
  print(mul())
 elif  l == "/":
  print(div())
 elif l == ";":
     name = name.capitalize()
     print("thank you {} for visiting  python we hope you visit us again.".format(name))
     # exit(0)

 else:
      print("wrong symbol entered....")
