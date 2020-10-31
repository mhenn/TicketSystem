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


        effective = [x['name'] for x in m_mapping if x['name'] in relevant and action in x['actions'] ] 
        print(f'effective: {effective}')
        # get user for mapping
        params = {'data' : effective }
        r = requests.get('http://localhost:5555/config/mail/', headers=header, params=params)

        mail_list = json.loads(r.content)
        # TODO edit recipient list gathered from config service. 
        # TODO Think about saving the config localy and updating it via message broker
       
        
        ticketId = content['message']['ticketId']
        mails = {}
        
        for recipient in mail_list:
            print(f'ayoo {recipient}')
            msg = MIMEText(f'The Ticket {ticketId} has been {action}')
            msg['To'] = email.utils.formataddr(('Recipient',recipient))
            msg['From'] = email.utils.formataddr(('Author','ticket-service@example.com'))
            msg['Subject'] = 'Ticket Notification'
            mails[recipient] = msg.as_string()

        return mails


    def send_mail(self, mail, recipient):
        server = smtplib.SMTP('127.0.0.1', 1025)
        server.set_debuglevel(True)  # show communication with the server
        print(recipient)
        try:
            server.sendmail('ticket-service@example.com',[recipient],mail)
        except Exception as e:
            print(e)

