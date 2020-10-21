import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
    'author@example.com'))
msg['Subject'] = 'Simple test message'

content = msg.as_string()

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('author@example.com',
            ['Mikeianhenning93@gmail.com'],content)
except Exception as e:
    print(e)
