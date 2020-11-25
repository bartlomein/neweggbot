import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_func(items):
    content = ''
    for item in items:
        content += item + '\n'
    # The mail addresses and password
    sender_address = ''
    sender_pass = ''
    receiver_address = ''
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    # The subject line
    message['Subject'] = '3080 BOT FOUND A NEW ONE'
    # The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
