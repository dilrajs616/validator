import ssl
import smtplib
from email.message import EmailMessage

async def sendEmail(reciever_mail, subject, body):
    sender_mail = 'gndecauthenticator@gmail.com'
    password = 'nrdl hxyq cksi zthy'

    em = EmailMessage()
    em["From"] = sender_mail
    em["to"] = reciever_mail
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_mail, password)

            # Send the email and check the response
            response = smtp.sendmail(sender_mail, reciever_mail, em.as_string())

            # Check if the response is empty (which means no errors occurred)
            if not response:
                return True  # No errors from the server
            else:
                return False  # Response contains error codes
    except smtplib.SMTPRecipientsRefused:
        return False  # Recipient was rejected (invalid email)
    except smtplib.SMTPAuthenticationError:
        return False  # Authentication failed (invalid login)
    except smtplib.SMTPException as e:
        return False  # Other SMTP errors
