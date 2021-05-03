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
        db = Connection()
        post_data = request.get_json()
        email = post_data['email']
        username = post_data['username']
        password = post_data['password']
        user = User(email, username, password)
        #Encrypting the password
        password, hashed = db.encrypt_pass(user)
        user_created = db.insert(user, hashed)
        return jsonify(user_created)

#This route take the user to the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #creating the db object 
        db = Connection()
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        print(username)
        print(password)
        #Checking to see if the user is in the database
        # flag, not_found, password_no_match = db.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        # if flag == True:
        #     #If the user is in the database, the user gets sent to the index page.
        #     session['username'] = request.form['username']
        #     #Sending the user into the app
        #     return redirect(url_for('landing'))
        # else:
        #     #If the user is not in the database then they will be sent to the
        #     #sign up page.
        #     if not_found:
        #         flash('Username not found, maybe sign up!')
        #     elif password_no_match:
        #         flash('Password does not match! Maybe sign up!')
    return jsonify('5')

if __name__ == '__main__':
    app.run()