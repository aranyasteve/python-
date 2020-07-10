print("welcome factorial calculator!")
print("first let us know about you .")
a = input("enter you name ")
a=a.capitalize()
b = int(input("enter you age"))
if b < 13:
    print("sorry....you are two young to use this calculator")
    exit(0)
print("thank you for the information {}".format(a))
c = int(input("enter a number "))


def fact(a):
    factorial=1
    for i in range(a, 1, -1):
        factorial=factorial*i
        print(factorial)

    print("thank you,for choosing us!")
    print("your answer is the addition of all the numbers above .")
fact(c)
