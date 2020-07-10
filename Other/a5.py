import random

def check():
    global n
    if a == [ ]:
        print("Game over no more choice left !")
        n = ";"
        exit(0)
a = ["maharashtra", "manipur", "gujrat", "uttar pradesh", "mizoram", "assam", "punjab", "harayana", "kashmir", "ladhak",
     "uttrakhand", "madhya pradesh", "goa", "karnatika", "kerala", "bihar", "andhra pradesh", "odisha", "chhattisgarh",
     "nagaland", "tripura", "meghalay", "himanchal pradesh", "arunanchal pradesh", "bihar", "telengana",
     "sikkim", "west bengal", "rajasthan", "jharkhand", "tamil nadu", "delhi"]

n = " "
print("Welcome to India  Atlas Game ")
print("The rules are very  easy \nYou have to enter any state in india ")
print("If you wish to exit \nyou can press ; any time")
b = input("enter your state choice ")
while n != ";":
    if b in a:
        a.remove(b)
        check()
        c = random.choice(a)
        print("my choice is", c)
        a.remove(c)
        check()
        b = input("enter your choice now  ")
        continue
    elif b==";":
        print("Thank you for playing!")
        break
    else:
        print("Error The name which you have entered in not in india or is alredy used by you or me")
        b = input("enter your state choice")
        continue




