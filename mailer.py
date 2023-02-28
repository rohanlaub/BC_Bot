from email.message import EmailMessage
import ssl
import smtplib


def send_email(sender: str, passw: str, receiver: str, cclist: list[str], subject: str, body: str):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em['CC'] = cclist
    em.set_content(body)

    # ssl : security
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, passw)
        smtp.sendmail(sender, receiver, em.as_string())
