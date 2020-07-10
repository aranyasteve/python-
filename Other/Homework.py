a = input("enter the name of the student")
b = input("enter the class of  {}".format(a))
c = float(input("enter the exam marks of {}".format(a)))
if c < 0:
    print("please enter the marks out of 500")
    d = 0

elif c <= .4 * 500:
    print("fail")
    d = "Fail"
elif c <= .5 * 500:
    d = "C"
elif c <= .6 * 500:
    d = "C+"
elif c <= .7 * 500:
    d = "B"
elif c <= .8 * 500:
    d = "B+"
elif c <= .9 * 500:
    d = "A"
elif c <= 500:
    d = "A+"
else:

    d = "Invalid entry...."
#     output
print("name is {}".format(a))
print("class is {}".format(b))
print("grade is {}".format(d))




