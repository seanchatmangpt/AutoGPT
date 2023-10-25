# Import the necessary modules
import smtplib
from email.message import EmailMessage

# Define the email sender and recipient
sender = "sender@example.com"
recipient = "recipient@example.com"

# Create the email message
msg = EmailMessage()
msg["Subject"] = "Test email"
msg["From"] = sender
msg["To"] = recipient
msg.set_content("This is a test email notification.")

# Connect to the SMTP server and send the email
with smtplib.SMTP("localhost") as smtp:
    smtp.send_message(msg)
