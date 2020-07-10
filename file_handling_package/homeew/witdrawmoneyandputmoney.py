import pymysql
conection3 = pymysql.connect('127.0.0.1', 'root', 'root', 'SBI')
cursor3 = conection3.cursor()
print("do you want to withdraw or deposit on your account ?")
print("if yes type 'withdraw'or 'deposit")
f = input().lower()
if f == "withdraw":
    h = input("enter your id")
    v = int(input("enter how much you want to withdraw"))
    d = int(input("enter your balance"))
    balance = d-v
    command5 = '''UPDATE account set  balance={},deposit=0  where taskid={}'''.format(balance,h)
    try:
        cursor3.execute(command5)
        cursor3.commit()
        print("done")
    except Exception as e:
        print("error:{}".format(e))

if f == "deposit":
    h = input("enter your id")
    v = int(input("enter how much you want to deposit"))
    d = int(input("enter your balance"))
    balance = d+v
    command5 = '''UPDATE account set  balance={},deposit=0  where taskid={}'''.format(balance,h)
    try:
        cursor3.execute(command5)
        print("done")
    except Exception as e:
        print("error:{}".format(e))

