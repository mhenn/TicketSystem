import smtplib
import email.utils
from email.mime.text import MIMEText
import requests
import json

class Logic():

    def __init__(self, db, service):
        self.db = db
        self.token = service
	   
    def prepare_mail(self, content):
        message = content['message']
        action = message['actions']
        tId = message['ticketId']
        token = self.token.get()


        header = {'Authorization': 'Bearer ' + token}
        
 
        header = {'Authorization': 'Bearer ' + token}
        r = requests.get('http://localhost:5000/ticket-service/ticket/' + tId , headers=header)
        ticket = json.loads(r.content)
        ticket = ticket['ticket'][0]
        to = ticket['to']
        
        # get Mappings where to is contained 
        r = requests.get('http://localhost:5555/config/mail-mapping/' , headers=header)
        m_mapping = json.loads(r.content)
        m_mapping = m_mapping['mapping']

        r = requests.get('http://localhost:5555/config/role-mapping/', headers=header)
        r_mapping = json.loads(r.content)
        r_mapping = r_mapping['mapping']
        relevant = [ x['name'] for x in r_mapping if to in x['children']]


        print('AYEEEEEEEEEEE')
        print(m_mapping)
        print(r_mapping)
        print(relevant)

        effective = [x for x in m_mapping if x['name'] in relevant and action in x['actions'] ] 
        print(f'effective: {effective}')
        # get user for mapping
        params = {'data' : action}
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

