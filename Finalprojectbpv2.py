'''
Final project Basic Py batch 11
send email to multiple recipients
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#definisi pengirim & penerima
from_addr = "tespython11@gmail.com"
to_addrs = ["John@example.com", "Mike@example.com"]
password = "pybasic11"

f = open("receiver.txt","w")
f.write = (to_addrs)
f.close()

#main
msg = MIMEMultipart()
msg["From"]    = from_addr
msg["To"]      = to_addrs
msg["Subject"] = "Final Project"

body = '''\Welcome... 
Final project Basic py batch 11 sent...
.
.
.
this is just a simple text to send
'''
msg.attach(MIMEText(body))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_addr, password)

text = msg.as_string() 
server.sendmail(from_addr, to_addrs, text)

server.quit()
