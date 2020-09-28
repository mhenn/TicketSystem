from interface import Interface



class IDatabase(Interface):


	def __init__(self):
		self.setup()


	def setup(self):
		pass


	def create(self, publisher):
		pass

		
	def delete_publisher(self, publisher):
		pass

	def delete_subscriber(self, publisher, subscriber):
		pass


	def get_publishers(self):
		pass	
		
	def get_publisher(self, publisher):
		pass

	def get_subscriber(self, publisher, subscriber):
		pass

	def add_subscriber(self, publisher, sub):
		pass
