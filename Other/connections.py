import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'student')
b = a.cursor()
everything = "select * form stse "
b.execute(everything)
c = b.fetchall()
print(c)


