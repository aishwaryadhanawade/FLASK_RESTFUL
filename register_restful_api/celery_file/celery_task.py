from register_restful_api import celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from register_restful_api import app

load_dotenv()


@celery.task()
def send_mail(email, msg_token):
    try:
        sender_mail = os.environ['sender_gmail']
        sender_password = os.environ['app_password']
        # sender_mail = 'aishwaryadhanawade612@gmail.com'
        # sender_password = 'igxnzbkbjtnctwio'

        message = MIMEMultipart("alternative")
        message['Subject'] = "Verification Email"
        message['From'] = sender_mail
        message['To'] = email

        message_link = MIMEText(msg_token, 'html')
        message.attach(message_link)

        smtpobj = smtplib.SMTP("smtp.gmail.com", 587)

        smtpobj.starttls()
        smtpobj.login(sender_mail, sender_password)
        smtpobj.sendmail(sender_mail, email, message.as_string())
    except Exception as e:
        raise Exception(str(e))
