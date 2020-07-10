from project.database import *
import pymysql
db1 = pymysql.connect('127.0.0.1', 'root', 'root', '{}'.format(a))
l = db1.cursor()
b=input("enter the table name you want to create ")
command2 ="""CREATE TABLE IF NOT EXISTS {}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        school VARCHAR(500)NOT NULL,
         maths_grade VARCHAR(5)NOT NULL,
         science_grade VARCHAR(5)NOT NULL,
         language_grade VARCHAR(5)NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)      ENGINE=INNODB """.format(b)
try:
    l.execute(command2)
    db1.commit()
    print("done")
except Exception as e:
    print("error:{}".format(e))
