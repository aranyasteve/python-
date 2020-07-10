from project.ceatetable import *
from project.database import *
import pymysql
db2 = pymysql.connect('127.0.0.1', 'root', 'root', '{}'.format(a))
l1 = db2.cursor()
for a in range(int(input("enter how many records "))):
    name = input("Enter your name ")
    age = int(input("enter yor  age"))
    school = input("enter school name ")
    maths = input("enter maths grade")
    science = input("enter science grade")
    language = input("enter language grade")
    command3 = """INSERT INTO {}(name,age,school,maths_grade,science_grade,language_grade)
    VALUES('{}',{},'{}','{}','{}','{}');
    """.format(b, name, age, school, maths, science, language)

    try:
        l1.execute(command3)
        db2.commit()
        print("done")
    except Exception as e:
        print("error:", e)

