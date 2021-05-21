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
		text = text_file.read()
		return TextBlob(text)
	
	def get_sentiment_values_of_single_speech(self, text_converted):
		sentiment_sentence_list = []
		sentence_and_sentiment_list = []
		count = 0
		first_sentence = ''
		first_sentence_sentiment = 0
		for sentence in text_converted.sentences:
			sentence_and_sentiment = {}
			if count == 0:
				first_sentence = sentence
				first_sentence_sentiment = format(sentence.sentiment[0], '.3f')
			sentence_sentiment = sentence.sentiment[0]
			sentiment_sentence_list.append(sentence_sentiment)
			sentence_and_sentiment['sentence'] = sentence 
			sentence_and_sentiment['sentiment'] = sentence_sentiment
			sentence_and_sentiment_list.append(sentence_and_sentiment)
			count += 1
		print(sentence_and_sentiment_list)
		return sentiment_sentence_list, first_sentence, first_sentence_sentiment
	
	def get_sentiment_average_per_speech(self, sentiment_sentence_list):
		return format(sum(sentiment_sentence_list) / len(sentiment_sentence_list), '.3f')
	
	def get_text_file_sentiment(self):
		text_file = self.getting_text_file()
		text_converted = self.get_text_to_textBlob_format(text_file)
		sentiment_sentence_list, first_sentence, first_sentence_sentiment = self.get_sentiment_values_of_single_speech(text_converted)
		sentiment_speech_average = self.get_sentiment_average_per_speech(sentiment_sentence_list)
		return sentiment_speech_average, first_sentence, first_sentence_sentiment


#Ideas for sentence sentiment:
# Get all sentences and sentiment when the file is uploaded. 
# Send that over to client side 
# When user changes sentence is only refs client side and does not make a trip to the server. 

#Goals: 
# I need to get the speech name - which in this case is the file name - DONE
# I need to get the overall sentiment of the speech - DONE 
# I need to get the first sentence of the speech - DONE 
# I need to get the sentiment of that first speech - DONE
# I need to build a word chart of the text file 
# I neeed to build a chart of the sentiment by sentence 