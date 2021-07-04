import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()
# everything = "select * form stse "
# b.execute(everything)
# c = b.fetchall()
# print(c)
print("Hello, Got a new product ?\nNo worries you can store all the product information here")
print("So lets start")
a1 = input("Enter the name of your Product ")
c = input("Enter the company name ")
d = input("Enter the date you purchased this product ")
e = input("Enter the order Number of this product")
f = input("Enter the model Number of this product ")
g = input("Enter the serial number of this product ")

try:
    query = """INSERT INTO models (Name, Company, D_O_P, Order_No, Model_No, Serial_No) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(a1, c, d, e, f, g)
    b.execute(query)
    print("Your request is successfully done Thank you")
    a.commit()
    a.close()
except Exception as e:
    a.rollback()
    print(f"Sorry an error occured {e}")