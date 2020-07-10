import pymysql
db = pymysql.connect('127.0.0.1', 'root', 'root')
cus = db.cursor()
a = input("enter the name of the database you want to create.")
command = "create database if not exists {} ".format(a)
try:
    cus.execute(command)
    print("database created")
except Exception as e:
    print("error:{}".format(e))



