#This file will have the class that will create the user object 

class User():

	#Here I describe all the properties that each user object will have
	def __init__(self):
			self.username = ''
			self.email = ''
			self.password = ''

	#This method will add the properties to the user object. (Probably could have done this in the init method. I will state
	#that I feel like a complete moron for creating this method. It could have all been done above in the init method. This 
	#is what happens when your not paying attention! I leave this here as a lesson!)
	def set_up_user(self, username, email, address, city, state, zipcode, person_type, password):
			self.username = username
			self.email = email
			self.password = password