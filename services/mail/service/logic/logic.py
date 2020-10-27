import smtplib
import email.utils
from email.mime.text import MIMEText
import requests


class Logic():

    def __init__(self, db, service):
        self.db = db
        self.token = service
	   
    def prepare_mail(self, content):
        action = content['message']['actions']
        
        token = self.token.get()
        header = {'Authorization': 'Bearer ' + token}
        params = {'data': ['1','2','3'] }
        requests.get('http://localhost:5555/config/user/', headers=header, params=params)

        # TODO edit recipient list gathered from config service. 
        # TODO Think about saving the config localy and updating it via message broker

        ticketId = content['message']['ticketId']

        msg = MIMEText(f'The Ticket {ticketId} has been {action}')
        msg['To'] = email.utils.formataddr(('Recipient',
            'recipient@example.com'))
        msg['From'] = email.utils.formataddr(('Author',
            'author@example.com'))
        msg['Subject'] = 'Simple test message'

        return msg.as_string()



    def send_mail(self, mail):
        server = smtplib.SMTP('127.0.0.1', 1025)
        server.set_debuglevel(True)  # show communication with the server
        try:
            server.sendmail('author@example.com',['Mikeianhenning93@gmail.com'],mail)
        except Exception as e:
            print(e)

