import pymysql
db = pymysql.connect('127.0.0.1', 'root', 'root','job')
a = db.cursor()
query = "select * from job"
a.execute(query)
data=a.fetchall()
print(data)




