# Import the necessary modules
import smtplib
from email.mime.text import MIMEText

# Define the email sender and recipient
sender = 'sender@example.com'
recipient = 'recipient@example.com'

# Define the email content
message = MIMEText('This is a test email.')
message['Subject'] = 'Test Email'
message['From'] = sender
message['To'] = recipient

# Set up the SMTP server
smtp_server = smtplib.SMTP('smtp.example.com', 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login('username', 'password')

# Send the email
smtp_server.sendmail(sender, recipient, message.as_string())
smtp_server.quit()