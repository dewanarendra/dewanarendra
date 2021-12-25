#finalproject BasicPython batch 11
#program send email to multiple recipients


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

pengirim = "me@example.com"
list_penerima = ["John@example.com, Mike@example.com"]
penerima = ",".join(list_penerima)

pesan = MIMEMultipart()
pesan ["Subject"]    = "Final Project"
pesan ["From"]       = pengirim     #pengirim
pesan ["To"]         = penerima     #penerima
pesan ["cc"]         = " "

body = MIMEText("final_project")

pesan.attach(body)

smtp = smtplib.SMTP("dewa@example.com")
smtp.sendmail(pesan["From"], pesan["To"].split(",") + pesan["cc"].split(","), pesan.as_string())
smtp.quit()

