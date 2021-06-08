# libraries for use in project
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import datetime

#Importing files that I created for the project
from user import *
from db import *
from text import *

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
        login_values = {}
        #Checking to see if the user is in the database
        login_flag, not_found, password_no_match = db.check(username, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
    return jsonify(login_values)

#This route will handle the text analysis file upload
@app.route('/text_file_upload', methods=['GET', 'POST'])
def text_file_upload():
    if request.method == 'POST':
        if request.files:
            # For reference 
            # print(os. getcwd()) Used to get path to upload to 
            text_data = {}
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join('/Users/mikecuddy/Desktop/coding/data_science_projects/data_tool/server/text', filename))
            text_data['file_name'] = filename
            text_object = Text(filename)
            sentiment_graph_data, sentiment_speech_average, first_sentence, first_sentence_sentiment, sentence_and_sentiment_list, word_count_chart_data = text_object.get_text_file_sentiment()
            text_data['sentiment_speech_average'] = sentiment_speech_average
            text_data['first_sentence'] = str(first_sentence)
            text_data['first_sentence_sentiment'] = first_sentence_sentiment
            text_data['sentence_and_sentiment_list'] = sentence_and_sentiment_list
            text_data['sentiment_graph_data'] = sentiment_graph_data
            text_data['word_count_chart_data'] = word_count_chart_data
        return jsonify(text_data)

#This route will handle changing the word count on the word count graph
@app.route('/change_word_count', methods=['GET', 'POST'])
def change_word_count():
    if request.method == 'POST':
        post_data = request.get_json()
        text_object = Text(post_data['text_file_name'])
        text_file = text_object.getting_text_file()
        text_converted = text_object.get_text_to_textBlob_format(text_file)
        words_list = text_converted.words
        words = text_object.purge_extra_characters(words_list)
        word_and_count = text_object.clean_word_list(words, int(post_data['wordCount']))
        word_count_chart_data = text_object.buildChartData(word_and_count, words)
        return jsonify(word_count_chart_data)


if __name__ == '__main__':
    app.run()