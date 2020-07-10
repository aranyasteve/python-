import pymysql
conection1 = pymysql.connect('127.0.0.1', 'root', 'root', 'SBI')
cursor1 = conection1.cursor()
command1 = "CREATE TABLE IF NOT EXISTS  account(" \
         "account_id  INT AUTO_INCREMENT PRIMARY KEY," \
         "name VARCHAR(100)NOT NULL," \
         "phone_number INT(11) NOT NULL,"\
         "aadhar_card_id INT(50)NOT NULL," \
         "pan_number INT(50)NOT NULL," \
         "deposit INT(50)NOT NULL," \
         "balance INT(50) NOT NULL," \
         "create_dat TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
try:
    cursor1.execute(command1)
except Exception as e:
    print("error", e)