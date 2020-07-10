l = ''
while l != ";":
    try:
       a, b=input("enter two number").split(",")
       a = float(a)
       b = float(b)
       c = a/b
       print(c)
    except Exception as e:
       print("error:", e, "Try again")
       continue
    else:
        print("thank you")
        break
