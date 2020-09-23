from interface import Interface 


class ILogic(Interface):

	def __init__(self):
		pass
		
	def delete(self, ticketID):
		pass

	def update(self, ticket, ticketID):
		pass

	def create(self, ticket):
		pass
	
	def get(self):
		pass
