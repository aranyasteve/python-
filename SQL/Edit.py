import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()

print("Hello want to edit something?\n Don't worry you only need to enter the product name and"
      " you can edit what you want to edit")
a1 = input("Enter the product name")

b1 = input(f"Ok, Please tell what do you wish to update in {a1} ").lower()

s = ""
while s != ";":
    if b1 == "name":
        c1 = input("Please enter the new name of your model ")
        query = f"UPDATE models SET Name= '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    elif b1 == "d.o.p":
        c1 = input("Please enter the new purchase date of your model ")
        query = f"UPDATE models SET D_O_P = '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    elif b1 == "serial number":
        c1 = input("Please enter the new serial number of your model ")
        query = f"UPDATE models SET Serial_No = '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    elif b1 == "order number":
        c1 = input("Please enter the new order number of your model ")
        query = f"UPDATE models SET Order_No = '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    elif b1 == "model number":
        c1 = input("Please enter the new model number of your model ")
        query = f"UPDATE models SET Model_No = '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    elif b1 == "company":
        c1 = input("Please enter the new company  name of your model ")
        query = f"UPDATE models SET Company = '{c1}' WHERE Name = '{a1}'"
        b.execute(query)
        a.commit()
        print("Your request is done")
        break

    else:
        print("Sorry please chose a correct option")
        b1 = input(f"Please tell what do you wish to update in {a1} ").lower()
        continue



