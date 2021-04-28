#This file will have the class that will create the user object 

class User():

	#Here I describe all the properties that each user object will have
	def __init__(self, username, email, password):
			self.email = email
			self.username = username
			self.password = password