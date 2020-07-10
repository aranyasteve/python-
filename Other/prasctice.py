from Other.functionsforp import *
print("welcome to calculater")
name = input("enter your name")
name = name.capitalize()
print('''+ for addition\n- for subtraction\n* for multiplication \n/ for division\n % for mod \nfact for factorial\n= for result\n; for exit''')
print("enter your choice")
l=""
while l !=";":
 opt = input("").lower()
 if opt == "+":
     n=""
     while n != ";":
         try:
          a, b = input("enter two numbers through ,").split(",")
          a=int(a)
          b=int(b)
          result=add(a,b)
         except:
             print("error.....try again ")
             continue
         else:
             break

 elif opt == "=":
    print(result)
 elif opt == "*":
     n=""
     while n != ";":
         try:
             a,b=input("enter two number through ','").split(",")
             a=int(a)
             b=int(b)
             result = mul(a,b)
         except:
             print("error..... try again")
             continue
         else:
             break
 elif opt =="/":
     n=''
     while n != ";":
        try:
          a, b = input("enter two number through ','").split(",")
          a = int(a)
          b = int(b)
          result = div(a, b)
        except:
            print("error.....try again")
            continue
        else:
            break

 elif opt =="-":
     n=""
     while n != ";":
        try:
          a, b = input("enter two number through ','").split(",")
          a = int(a)
          b = int(b)
          result = sub(a, b)
        except:
            print("error.....try again")
            continue
        else:
            break
 elif opt =="%":
     n=""
     while n != ";":
        try:
          a, b = input("enter two number through ','").split(",")
          a = int(a)
          b = int(b)
          result = mod(a, b)
        except:
            print("error..... try again")
            continue
        else:
            break
 elif opt =="fact":
     n=""
     while n != ";":
         try:
             a=int(input("enter a number"))
             result = fact(a)
         except:
             print("error.....try again")
         else:
             break
 elif opt == ";":
     name = name.capitalize()
     print("thank you for choosing python", name)
     break

 else:
     print("syntax error  or wrong choice enter a symbol")
     continue




