'''
Final project Basic Py batch 11
send email to multiple recipients
'''

import smtplib

#definisi pengirim & penerima
from_addr = "tespython11@gmail.com"
to_addrs = ["johm@example.com","mike@example.com"]

password = "pybasic11"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_addr, password)

msg = "Sending email using python"
subject = "Final project"
body = "Subject : {}\n\n{}".format(subject,msg)


server.sendmail(from_addr,to_addrs,body)

server.quit()
