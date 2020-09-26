import requests
import json 
import time 

class Logic:

	def __init__(self):
		self.service_token = ServiceToken()	

#content = json.loads(message.data)['body']
#token = self.service_token.get_token()


	def get_ticket(self):
		token = self.service_token.get_token()

		header = {'Authorization': 'Bearer ' + token }
		r = requests.get('http://localhost:5000/ticket/', headers=header)		
		print(r.json())

	def post_ticket(self, ticket):	
		ticket = json.load(ticket)['']
		token = self.service_token.getTocken()
		header = {'Authorization': 'Bear ' + token}
		r = requests.post('http://localhost:5000/ticket/', headers=header, data=ticket)
		print(r.json())



class ServiceToken:

	def __init__(self):
		self.duration = 250
		self.time_received = 0
		self._access_token = ''	

	def get_token(self):

		current_time = time.time() -self.time_received 	

		if not self._access_token or current_time >= self.duration: 
			url = 'http://localhost:8000/auth/realms/Odonata/protocol/openid-connect/token'
			data= {'grant_type': 'password', 'client_id':'ticket-client', 'username':'mhenn', 'password':'mhenn'}
			response = requests.post(url, data=data)
			if response.status_code != 200:
				return False
			
			j_response = response.json() 
			self.duration = j_response['expires_in']
			
			self.time_received = time.time()
			self._access_token = j_response['access_token']
			return self._access_token
