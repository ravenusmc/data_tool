#This file will handle the connection to the database 

#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector

class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3306,
                                database='data_tool')
        self.cursor = self.conn.cursor()

    def pull_user_info(self, username):
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        return row
    
    #This method will encrypt the password
    def encrypt_pass(self, user):
        password = user.password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed
    
    #This method will insert a new user into the database.
    def insert(self, user, hashed):
        user_created = True
        self._SQL = """insert into users
          (email, username, password)
          values
          (%s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.username, user.email, hashed))
        self.conn.commit()
        return user_created
    
    #This method will check to ensure that the username is in the database.
    def check(self, username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        #Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        user = {}
        user["id"] = row[0]
        user['username'] = row[1]
        user['email'] = row[2]
        #Here I check to see if the username is in the database.
        if str(row) == 'None':
            login_flag = False
            not_found = True
            password_no_match = False
        #If the user name is in the database I move here to check if the password
        #is valid.
        else:
            hashed = row[3].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == str(hashed,'UTF-8'):
                login_flag = True
                not_found = False
                password_no_match = False
            #This is a final catch all area. Basically if the password does not match 
            #the user is not getting in. 
            else:
                login_flag = False
                not_found = False
                password_no_match = True
        return login_flag, not_found, password_no_match, user
    
    def check_password(self, user_id, password):
        password = password.encode('utf-8')
        query = ("""SELECT * FROM users WHERE user_id = %s""")
        self.cursor.execute(query, (user_id,))
        row = self.cursor.fetchone()
        hashed = row[3].encode('utf-8')
        if bcrypt.hashpw(password, hashed) == str(hashed,'UTF-8'):
            password_match = True
        else:
            password_match = False 
        return password_match

