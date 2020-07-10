a=input("enter a symbol")
if a =="+":
    l=''
    while l != ";":
     try:
        b, c = input("enter two numbers thorough ,").split(",")
        b = int(b)
        c = int(c)
        print(c+b)
     except:
        print("error try again")
        continue
     else:
        print("thank you")
        break
if a =="-":
    l=''
    while l != ";":
     try:
        b, c = input("enter two numbers thorough ,").split(",")
        b = int(b)
        c = int(c)
        print(b-c)
     except:
        print("error try again")
        continue
     else:
        print("thank you")
        break
if a =="*":
    l=''
    while l != ";":
     try:
        b, c = input("enter two numbers thorough ,").split(",")
        b = int(b)
        c = int(c)
        print(c*b)
     except:
        print("error try again")
        continue
     else:
        print("thank you")
        break
if a =="/":
    l=''
    while l != ";":
     try:
        b, c = input("enter two numbers thorough ,").split(",")
        b = int(b)
        c = int(c)
        print(c/b)
     except:
        print("error try again")
        continue
     else:
        print("thank you")
        break

