import ssl
import smtplib
from email.message import EmailMessage

async def sendEmail(reciever_mail, subject, body):
    sender_mail = 'dilraj082@gmail.com'
    password = 'saxp avnu udiq gnis'

    em = EmailMessage()

    em["From"] = sender_mail
    em["to"] = reciever_mail
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_mail, password)
        smtp.sendmail(sender_mail, reciever_mail, em.as_string())