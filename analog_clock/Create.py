import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()
# everything = "select * form stse "
# b.execute(everything)
# c = b.fetchall()
# print(c)
print("Hello, Got a new product ?\nNo worries you can store all the product information here")