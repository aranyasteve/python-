# from project.writeintable import *
import pymysql
db3 = pymysql.connect('127.0.0.1', 'root', 'root', 'students')
l2 = db3.cursor()
command4 = "select * from aranya "
try:
    l2.execute(command4)
    data = l2.fetchall()
    print("you have written ", data)
    print("thank you ")
except Exception as e:
    print("error:", e)
finally:
        db.close()
        db1.close()
        db2.close()
        db3.close()
