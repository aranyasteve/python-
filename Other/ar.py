def aranya(a):
    if a > 100:
        print("congrats you have passed ")
    else:
        print("you have failed....")


b = int(input("enter  your marks: "))
if b > 200:
    print("ERROR...wrong marks entered.")
elif b <= 0:
    print("you have entered {} ,cannot make marks less or equal to zero.".format(b))
else:
    aranya(b)


    def aranya(a):
        if a > 100:
            return"congrats you have passed "
        else:
            return"you have failed...."


    b = int(input("enter  your marks: "))
    if b > 200:
        print("ERROR...wrong marks entered.")
    elif b <= 0:
        print("you have entered {} ,cannot make marks less or equal to zero.".format(b))
    else:
        print(aranya(b))






