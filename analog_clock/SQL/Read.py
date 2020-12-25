import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()
# everything = "select * form stse "
# b.execute(everything)
# c = b.fetchall()
# print(c)
print("Hi There want to see the details of your product?\nNo worries you just need to enter the Name here and "
      "you will get everything")
a1 = input("Enter the name of the Product ")

query = f"SELECT * FROM  models  WHERE Name = '{a1}'"
try:
    b.execute(query)
    b1 = b.fetchall()
    print(b1)
    print("Here are your details")
    print("Name of the product ", b1[0][1])
    print("Company Name ", b1[0][2])
    print("Date Purchased this product ", b1[0][3])
    print("Order Number of this product ", b1[0][4])
    print("Model Number of this product  ", b1[0][5])
    print("Serial Number of this product  ", b1[0][6])
    print("Date entered this details ", b1[0][7])
    a.close()

except Exception as e:
    a.rollback()
    print(e)