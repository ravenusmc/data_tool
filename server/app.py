# libraries for use in project
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

#Importing files that I created for the project
from user import *
from db import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

#This route will take the user to the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Creating a user object 
        user = User()
        #creating the db object
        db = Connection()
        post_data = request.get_json()
        print(post_data)
        #setting the properties to the user object
        # user.set_up_user(username, email, address, city, state, zipcode, person_type, password)
        #Getting the lat and lng coordinates for the user. 
        # user = coords.get_coords(user)
        #Encrypting the password
        # password, hashed = db.encrypt_pass(user)
        # #Adding the user to the database
        # db.insert(user, hashed)
        return jsonify('hi Mike')

if __name__ == '__main__':
    app.run()