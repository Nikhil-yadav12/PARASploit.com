import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import os

# Set up email configuration
sender_email = "nikhilyadav79706@gmail.com"
sender_password = "bhbayxagkgtnvjdz"
recipient_email = "nikhilyadav12.ny@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create email message
subject = "Important Message from HR"
body = "Dear Employee,\n\nPlease click on the following link to verify your HR profile: http://parasploit.com\n\nThank you,\nHR Department"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print("Phishing email sent successfully!")
except:
    print("Error: Unable to send phishing email.")

# Personalization feature
recipient_name = "John Doe"
personalized_body = f"Dear {recipient_name},\n\nPlease click on the following link to verify your HR profile: http://fakehrverification.com\n\nThank you,\nHR Department"
msg.attach(MIMEText(personalized_body, 'plain'))

# Email tracking feature
now = datetime.datetime.now()
sent_time = now.strftime("%Y-%m-%d %H:%M:%S")
logfile = "email_log.txt"
with open(logfile, "a") as f:
    f.write(f"Sent at {sent_time} to {recipient_email}\n")

# Phishing templates feature
templates_dir = "templates"
if not os.path.exists(templates_dir):
    os.mkdir(templates_dir)
template_file = os.path.join(templates_dir, "hr_verification_template.txt")
with open(template_file, "w") as f:
    f.write(personalized_body)

# Reporting feature
log_data = []
with open(logfile, "r") as f:
    log_data = f.readlines()

num_emails_sent = len(log_data)
num_emails_opened = 0
num_links_clicked = 0

print("Phishing simulation report:")
print(f"Number of emails sent: {num_emails_sent}")

for line in log_data:
    if "opened" in line:
        num_emails_opened += 1
    if "clicked" in line:
        num_links_clicked += 1

print(f"Number of emails opened: {num_emails_opened}")
print(f"Number of links clicked: {num_links_clicked}")
