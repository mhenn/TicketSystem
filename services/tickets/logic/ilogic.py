from interface import Interface 


class ILogic(Interface):

	def __init__(self, db):
		pass
		
	def delete(self, ticketID):
		pass

	def update(self, ticket):
		pass

	def create(self, ticket):
		pass
