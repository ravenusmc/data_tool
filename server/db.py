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
    def encrypt_pass(self, post_data):
        password = post_data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed
    
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
    
    # This method will check to ensure that the username is in the database. It's also 
    # a method that I wrote a long time ago that really needs to be modified - essentially 
    # improved. 
    def check(self, username, password):
        # Setting up a user dictionary
        user = {}
        # I first encode the password to utf-8
        password = password.encode('utf-8')
        # Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        # Here I check to see if the username is in the database.
        if str(row) == 'None':
            print('here')
            login_flag = False
            not_found = True
            password_no_match = False
        # If the user name is in the database I move here to check if the password
        # is valid.
        else:
            hashed = row[3].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == str(hashed,'UTF-8'):
                user["id"] = row[0]
                user['username'] = row[1]
                user['email'] = row[2]
                login_flag = True
                not_found = False
                password_no_match = False
            # This is a final catch all area. Basically if the password does not match 
            # the user is not getting in. 
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
    
    def update_username_and_email(self, post_data):
        self._SQL = """UPDATE users SET username = %s, email = %s
        where user_id = %s"""
        self.cursor.execute(self._SQL, (post_data['username'], post_data['email'], post_data['id']))
        self.conn.commit()
    
    def update_password(self, post_data, hashed):
        self._SQL = """UPDATE users SET password = %s
        where user_id = %s"""
        self.cursor.execute(self._SQL, (hashed, post_data['id']))
        self.conn.commit()
    
    def delete_user(self, id):
        self._SQL = """DELETE FROM users WHERE user_id = %s"""
        self.cursor.execute(self._SQL, (id, ))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    
    # I don't really like creating this method - done in the check method but I'll keep this here 
    def get_user_information(self, post_data):
        self._SQL = ("""SELECT * FROM users WHERE user_id = %s""")
        self.cursor.execute(self._SQL, (post_data['id'],))
        row = self.cursor.fetchone()
        user = {}
        user["id"] = row[0]
        user['username'] = row[1]
        user['email'] = row[2]
        self.cursor.close()
        self.conn.close()
        return user



