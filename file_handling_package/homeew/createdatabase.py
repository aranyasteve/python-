import pymysql
conection = pymysql.connect('127.0.0.1', 'root', 'root')
cursor = conection.cursor()
command = " create database  SBI"
try:
    cursor.execute(command)
except Exception as e:
    print("error", e)