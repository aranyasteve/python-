import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender = "aranyashukla9@gmail.com"

reciever = "shuklastu7@gmail.com"

messag = MIMEMultipart()

messag["From"] = sender

messag["To"] = reciever

messag["Subject"] = "Email"

bod = "Hi i am Aranya and I am sending this mail with attaching something "

messag.attach(MIMEText(bod, "plain"))

file_name = "C:\\Users\\Aranya Shukla\\Downloads\\IMG_20200909_011007_2.jpg"
attach = open(file_name, "rb")

p = MIMEBase("application", "octet-stream")

p.set_payload((attach).read())

encoders.encode_base64(p)

p.add_header("Content-Disposition", f"attachment; filename={file_name}")

messag.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender, "933##st70")

text = messag.as_string()

s.sendmail(sender, reciever, text)

s.quit()

