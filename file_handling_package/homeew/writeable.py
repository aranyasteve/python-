import random
import pymysql
conection2 = pymysql.connect('127.0.0.1', 'root', 'root', 'SBI')
cursor2=conection2.cursor()
cursor3=conection2.cursor()
print("welcome to sbi bank")
print("to make your account fill the following details")
n = ""
while n !=";":
    try:
        a = input("enter yor name ")
        b=int(input("enter your aadhar card id" ))
        c = int(input("enter your pan card id"))
        d=input("enter amount you want to deposit (NOTE:cannot enter 0 or less than 0 amount ) ")
        n=";"
    except:
      print("error something wrong has happened to make sure you are safe try again form beginning")

e = random.randrange(1,1000)
# else:
#       print("thank you ")
#       n = ";"
command3='''INSERT INTO account(taskid,name, adhar_card_id,pannumber,deposit, balance)
         VALUES({},'{}',{},{},{},{})'''.format(e, a, b, c, d, d)
command4="select * from account"
try:
    cursor2.execute(command3)
    conection2.commit()
    print("your account is made your filled in details are:")
    cursor3.execute(command4)
    data=cursor3.fetchall()
    print(data)
    print("your id is ", e, "if you want to deposit or withdraw money you need to enter your id")

except Exception as e:
    print("error:{}".format(e))
