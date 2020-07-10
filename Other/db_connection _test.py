import pymysql
db = pymysql.connect('127.0.0.1', 'root', 'root', 'student')
b = db.cursor()
query = "select * from stse"

b.execute(query)
data = b.fetchall()
db.close()
print(data)
