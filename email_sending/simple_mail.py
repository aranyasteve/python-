import smtplib
from smtplib import SMTPException

sender = "ramnageena400@gmail.com"
recivers = ["aranyashukla9@gmail.com", "aranyashukla9@outlook.com", "ram.nageena@gmail.com"]

message=""" From:From Person <{}>
To:To Person <{}>
MIME-Version:1.0
Content-type:text/html
Subject:Sending Email Through Python code
Good Morning
Hello Sir this is to kindly inform you that your ward is doing really good in 
academic and co-curricular activities.
Thanking you
Director
""".format(sender,recivers[0])
try:
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login(sender, "asdf.123")
    smtp_obj.sendmail(sender, recivers, message)
    print("your requesrt is sone thank you for choosing python and i am highly ")
except SMTPException as e:
    print("error : message not sent ", e)