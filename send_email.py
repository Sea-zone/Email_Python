import smtplib
import ssl
from email.message import EmailMessage


email_sender = '' #enter your email address here
email_password = '' #enter your  passworde here

email_receiver = '' #enter the receivers email address

subject = 'Check out my new video'
body = """
I just published a new video on Youtube:
https://www.youtube.com/watch?v=eWLLudI8sZ8&t=292s
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# for the security purpose

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
except Exception as e:
    print(f"An error occurred: {e}")
