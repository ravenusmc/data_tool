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
        self._SQL = """insert into users
          (email, username, password)
          values
          (%s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.email, user.username, hashed))
        self.conn.commit()

# test = Connection() 
# name = test.pull_user_info('test')
# print(name[1])