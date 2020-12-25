import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("aranyashukla9@gmail.com", "933##st70")

message = "Mama,This is to inform you that I have successfully sent this email to you by Python "

s.sendmail("aranyashukla9@gmail.com", "aranyashukla9@outlook.com", message)

s.quit()

print("Done")