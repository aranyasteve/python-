import json


def read_file():
    with open("write.json") as foldy:
        return json.load(foldy)


def newacc():
    print("to create an account please enter the following details")
    l=["Name","Age","Your total %","grade","address","school name"]
    d={}
    for x in l:
        if x == "Age" or x == "Your total %":
            a=int(input(("enter your {}".format(x))))
            d[x]=a
        else:
            b=input(("enter your {}".format(x)))
            d[x]=b

    data=read_file()
    data=data[0]
    x = len(data)
    x = x+1
    x = str(x)
    a = {x: d}
    data.update(a)
    data = [data]
    lf=open("write.json", 'w')
    json.dump(data, lf)
    lf.close()
    print("your request is done.your id is {},to update or view your account you need to remember your id".format(x))


def update():
    a=input("enter your id")
    data = read_file()
    if a in data[0].keys():
        print("Hello {}!".format(data[0][a]["Name"].capitalize()))
        print("what you want to update ?'Name','Age','Your total %','Grade','Address','School Name' ")
        b=input("Enter what you want to update").lower()
        if b =="name":
            name=input("enter your new name")
            data[0][a]["Name"]=name
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        elif b == "age":
            age = input("enter your new age")
            data[0][a]["Age"] = age
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        elif b == "grade":
            grade = input("enter your new grade")
            data[0][a]["grade"] = grade
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        elif b == "address":
            address = input("enter your new address")
            data[0][a]["address"] = address
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        elif b =="school name":
            school = input("enter your new school")
            data[0][a]["school"] = school
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        elif b =="your total %" or b=="total %":
            total= input("enter your new %")
            data[0][a]["school"] = total
            lf = open("write.json", 'w')
            json.dump(data, lf, indent=4)
            lf.close()
        else:
            print('wrong choice entered try again latter ')


    else:
        print("Sorry invalid id entered try again latter for security purpose")


def see():
    id=input("enter your id ")
    data=read_file()
    if id in data[0].keys():
        print("Hello {}".format(data[0][id]["Name"].capitalize()))
        print("Your requested details are below")
        l = ["Name", "Age", "Your total %", "grade", "address", "school name"]
        for x in l:
            print("{} ==> {}".format(x,data[0][id][x]))
    else:
        print("In valid id....try again latter")



def dt():
    data = read_file()
    print(data[1]["1"]["math"])
