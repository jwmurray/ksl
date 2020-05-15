import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'john@gardenway.org'
sender_password = 'Lancer83'


# the sender's email
# FROM = email
# the receiver's email
receiver_address = 'jwmurray@alum.mit.edu'
receiver_address = 'rose@gardenway.org'
# TO   = 'jwmurray@alum.mit.edu'
# initialize the message we wanna send
msg = MIMEMultipart()
# set the sender's email
msg["From"] = sender_address
# set the receiver's email
msg["To"] = receiver_address
# set the subject
msg["Subject"] = "test email"
# set the body of the email
text = '''
Dear John,

I wanted to take a moment to write you a quick email.  I have been having a lot of trouble getting emails sent through gmail without getting a spam label. 

Let's see if this longer email will work.

John
'''

text = MIMEText(text, "plain")
# attach this body to the email
msg.attach(text)
print(msg.as_string())

# initialize the SMTP server
server = smtplib.SMTP("smtp-relay.gmail.com", 587)


# connect to the SMTP server as TLS mode (secure) and send EHLO
server.starttls()

# login to the account using the credentials
server.login(sender_address, sender_password)
# send the email
server.sendmail(sender_address, receiver_address, msg.as_string())
# terminate the SMTP session
server.quit()
print("Mail sent")