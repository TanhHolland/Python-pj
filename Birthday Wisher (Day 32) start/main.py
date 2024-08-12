import smtplib

my_email = "tanhduhieu2k@gmail.com"
password = "neaadonaxpgiusbn"

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls();
connection.login(my_email,password)

to_email = "nhoklilom2.0@gmail.com"

connection.sendmail(from_addr=my_email,to_addrs=to_email,msg="Hello")
connection.close()