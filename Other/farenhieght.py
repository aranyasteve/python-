a = int(input("Enter what do you want to convert if fahrenheit to celsius type f/c or celsius to fahrenheit c/f"))
print(a)
if a ==1:
    b=int(input("Enter fahrenheit"))
    formula=5/9*(b-32)
    print("Your answer is ",formula)
elif a== 2:
    b=int(input("Enter celsius"))
    formula=9/5*(b+32)
    print("your answer is ",formula)
else:
    print('wrong choice try again latter ')

