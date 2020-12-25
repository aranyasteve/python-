import pymysql
a = pymysql.connect('127.0.0.1', 'root', 'root', 'product')
b = a.cursor()

querry = """CREATE TABLE IF NOT EXISTS models (
         Sr_No INT AUTO_INCREMENT PRIMARY KEY,
         Name VARCHAR(100) NOT NULL,
         Company VARCHAR(100) NOT NULL,
         D_O_P  DATE,
         Order_No VARCHAR(50) NOT NULL,
         Model_No VARCHAR(50) NOT NULL,
         Serial_No VARCHAR(50) NOT NULL,
         Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP) ENGINE=INNODB"""
try:
    b.execute(querry)
    print("Done")
    a.close()

except Exception as E:
    print(f"Error {E}")