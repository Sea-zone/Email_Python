import smtplib
import ssl
import os
from email.message import EmailMessage

# Get sensitive information from environment variables
email_sender = os.environ.get('EMAIL_SENDER')
email_password = os.environ.get('EMAIL_PASSWORD')
email_receiver = ''  # Enter the receiver's email address

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

# for security purpose
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("SMTP Authentication Error: Check your email and password.")
except smtplib.SMTPException as e:
    print(f"SMTP Exception: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
