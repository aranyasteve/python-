# def nperson(name, age=0, address=None):
#     print("name is {} age is {} address is {}".format(name, age, address))
#     return name, age, address
#
# a = input("enter name : ")
# b = input("enter age : ")
# c = input("Enter address : ")
#
# name,age, address = nperson(a, address=c, age=b)
# print(age)

def genral_store():
     print("200")
     return 100

def backary(rs):
    if  rs <500:
        return  "Cake not avalable"
    else:
        return "Cake is ready"


arnya = 300
g = genral_store()
print(g)
if g:
    arnya += g
print(backary(arnya))



