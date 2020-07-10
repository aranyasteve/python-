x = int(input("enter a no : ")); y = int(input("enter a no : ")); z = int(input("enter a no : "))
if x > y and x > z:
    print("{} is grater ".format(x))
elif y > z:
    print("{} is grater ".format(y))
else:
    print("{} is grater ".format(z))