from interface import Interface



class ITicketDatabase(Interface):


	def __init__(self):
		self.setup()


	def setup(self):
		pass


	def create(self, ticket):
		pass


	def update(self, ticket):
		pass

		
	def delete(self, ticketID):
		pass

	
	def get(self):
		pass
