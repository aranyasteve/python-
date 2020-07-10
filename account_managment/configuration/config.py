import pymysql

con = pymysql.connect('localhost', 'root', 'root', 'SBI')

coomando='''create table banking(id integer(13) auto_increment,
 name varchar(50),address varchar(100),phone_no varchar(11),
 aadhar varchar(14),pan varchar(10), balance float,open_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,primary key(id));
'''