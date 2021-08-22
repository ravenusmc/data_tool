# libraries for use in project
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import datetime

# Importing files that I created for the project
from user import *
from db import *
from text import *
from data import *
from data_helper import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        email = post_data['email']
        username = post_data['username']
        password = post_data['password']
        user = User(email, username, password)
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(user, hashed)
        return jsonify(user_created)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        login_values = {}
        # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db.check(
            username, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
        login_values['user'] = user
    return jsonify(login_values)


@app.route('/check_password', methods=['GET', 'POST'])
def check_password():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        password = post_data['originalPassword']
        user_id = post_data['id']
        password_match = db.check_password(user_id, password)
    return jsonify(password_match)


@app.route('/text_file_upload', methods=['GET', 'POST'])
def text_file_upload():
    if request.method == 'POST':
        if request.files:
            # For reference
            # print(os. getcwd()) Used to get path to upload to
            text_data = {}
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                '/Users/mikecuddy/Desktop/coding/data_science_projects/data_tool/server/text', filename))
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


@app.route('/change_word_count', methods=['GET', 'POST'])
def change_word_count():
    if request.method == 'POST':
        post_data = request.get_json()
        text_object = Text(post_data['text_file_name'])
        text_file = text_object.getting_text_file()
        text_converted = text_object.get_text_to_textBlob_format(text_file)
        words_list = text_converted.words
        words = text_object.purge_extra_characters(words_list)
        word_and_count = text_object.clean_word_list(
            words, int(post_data['wordCount']))
        word_count_chart_data = text_object.buildChartData(
            word_and_count, words)
        return jsonify(word_count_chart_data)


@app.route('/update_user_profile/<id>', methods=['PUT'])
def update_user_profile(id):
    if request.method == 'PUT':
        db = Connection()
        post_data = request.get_json()
        if post_data['password'] == '':
            db.update_username_and_email(post_data)
            user = db.get_user_information(post_data)
        else:
            hashed = db.encrypt_pass(post_data)
            db.update_password(post_data, hashed)
            user = db.get_user_information(post_data)
        return jsonify(user)


@app.route('/delete_user/<id>', methods=["DELETE"])
def delete_user(id):
    if request.method == 'DELETE':
        db = Connection()
        db.delete_user(id)
        return jsonify('')


@app.route('/fetch_File_Information', methods=['GET', 'POST'])
def fetch_File_Information():
    if request.method == 'POST':
        if request.files:
            data_information = {}
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                '/Users/mikecuddy/Desktop/coding/data_science_projects/data_tool/server/data', filename))
            data_object = Data(filename)
            data_file = data_object.getting_data_file()
            column_names = data_object.get_column_names(data_file)
            data_information['file_name'] = filename
            data_information['column_names'] = column_names
            # column_names_and_data_types = data_object.get_data_types(data_file)
            # data_information['file_data_types'] = column_names_and_data_types
        return jsonify(data_information)


@app.route('/build_data_graph', methods=['GET', 'POST'])
def build_data_graph():
    if request.method == 'POST':
        data_helper_obj = Data_Helper()
        data_graph_information = {}
        post_data = request.get_json()
        data_object = Data(post_data['payload']['fileName'])
        data_file = data_object.getting_data_file()
        # Checking for Unique Values - x axis
        unique_values = data_helper_obj.get_unique_values_x_axis(
            data_file, post_data)
        unique_values_length_x_axis = data_helper_obj.get_length_unique_values(
            unique_values)
        # Checking for unique Values - y axis
        unique_values_y_axis = data_helper_obj.get_unique_values_y_axis(
            data_file, post_data)
        if unique_values_length_x_axis > 8:
            if post_data['payload']['aggregateValue']:
                print('here')
                graph_data = data_object.get_column_data_for_graph_aggregate(
                    data_file, post_data, unique_values, unique_values_y_axis)
                graph_data = data_helper_obj.sort_graph_data(graph_data)
                data_graph_information['graph_data'] = graph_data
                data_graph_information['show_user_warning'] = False
                data_graph_information['show_graph'] = True
            else:
                data_graph_information['show_user_warning'] = True
        else:
            if post_data['payload']['uniqueValue'] == 'true':
                unique_values_y_axis = data_helper_obj.get_unique_values_y_axis(
                    data_file, post_data)
                graph_data = data_object.get_column_data_for_graph_unique_y_values(
                    data_file, post_data, unique_values, unique_values_y_axis)
            else:
                graph_data = data_object.get_column_data_for_graph(
                    data_file, post_data, unique_values)
            data_graph_information['show_user_warning'] = False
            data_graph_information['graph_data'] = graph_data
            data_graph_information['show_graph'] = True
        return jsonify(data_graph_information)


if __name__ == '__main__':
    app.run()
