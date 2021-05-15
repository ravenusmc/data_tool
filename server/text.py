# This file will deal with the text analysis part of the application 

#importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob
import fileinput

class Text():

	def __init__(self, file_name):
		self.file_name = file_name
	
	def getting_text_file(self):
		return open("./text/" + self.file_name, "r")
	
	def get_text_to_textBlob_format(self, text_file):
		text_file_converted = str([cell.encode('utf-8') for cell in text_file])
		return TextBlob(text_file_converted)
	
	def get_sentiment_values_of_single_speech(self, text_converted):
		sentiment_sentence_list = []
		for sentence in text_converted.sentences:
				sentence_sentiment = sentence.sentiment[0]
				sentiment_sentence_list.append(sentence_sentiment)
		return sentiment_sentence_list
	
	def get_sentiment_average_per_speech(self, sentiment_sentence_list):
		return sum(sentiment_sentence_list) / len(sentiment_sentence_list)
	
	def get_text_file_sentiment(self):
		text_file = self.getting_text_file()
		text_converted = self.get_text_to_textBlob_format(text_file)
		sentiment_sentence_list = self.get_sentiment_values_of_single_speech(text_converted)
		sentiment_speech_average = self.get_sentiment_average_per_speech(sentiment_sentence_list)
		return sentiment_speech_average
	
	def get_first_sentence_in_text_file(self):
		text_file = self.getting_text_file()
		text_converted = self.get_text_to_textBlob_format(text_file)
		count = 0
		first_sentence = ''
		for sentence in text_converted.sentences:
			if count == 0:
				first_sentence = sentence
				break
		return first_sentence
		print(sentence)


#Goals: 
# I need to get the speech name - which in this case is the file name - DONE
# I need to get the overall sentiment of the speech - DONE 
# I need to get the first sentence of the speech - DONE 
# I need to get the sentiment of that first speech 
# I need to build a word chart of the text file 
# I neeed to build a chart of the sentiment by sentence 