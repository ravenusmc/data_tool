# This file will deal with the text analysis part of the application 

# importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob
import fileinput
import re

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
			sentence_and_sentiment['sentence'] = str(sentence)
			sentence_and_sentiment['sentiment'] = format(sentence_sentiment, '.3f')
			sentence_and_sentiment_list.append(sentence_and_sentiment)
			count += 1
		return sentiment_sentence_list, first_sentence, first_sentence_sentiment, sentence_and_sentiment_list
	
	def get_sentiment_average_per_speech(self, sentiment_sentence_list):
		return format(sum(sentiment_sentence_list) / len(sentiment_sentence_list), '.3f')
	
	def get_data_for_sentiment_graph(self, text_converted):
			sentiment_graph_data = []
			columns = ['Sentence', 'Sentiment']
			sentiment_graph_data.append(columns)
			count = 0 
			for sentence in text_converted.sentences:
				rows = []
				sentence_sentiment = sentence.sentiment[0]
				sentence_number = count + 1
				rows.append(sentence_number)
				rows.append(float(format(sentence_sentiment, '.3f')))
				sentiment_graph_data.append(rows)
				count += 1
			return sentiment_graph_data

	def get_text_file_sentiment(self):
		text_file = self.getting_text_file()
		text_converted = self.get_text_to_textBlob_format(text_file)
		words_list = text_converted.words
		# The code here will be going to build the common words
		words = self.purge_extra_characters(words_list) 
		word_and_count = self.clean_word_list(words)
		word_count_chart_data = self.buildChartData(word_and_count, words)
		# End common words code 
		sentiment_graph_data = self.get_data_for_sentiment_graph(text_converted)
		sentiment_sentence_list, first_sentence, first_sentence_sentiment, sentence_and_sentiment_list = self.get_sentiment_values_of_single_speech(text_converted)
		sentiment_speech_average = self.get_sentiment_average_per_speech(sentiment_sentence_list)
		return sentiment_graph_data, sentiment_speech_average, first_sentence, first_sentence_sentiment, sentence_and_sentiment_list, word_count_chart_data

	def purge_extra_characters(self, words_in_list):
		words = []
		for word in words_in_list:
				word = re.split(r'[,\s.]', word)
				words.append(word[0])
		return words
	
	def clean_word_list(self, words_in_list, times_word_appears = 3):
		word_and_count = {}
		len_count = 0
		# Removing periods and commas at the end of each word
		words = self.purge_extra_characters(words_in_list)
		while len_count < len(words):
				rows = []
				word_count = 0
				# Assign the current_word to the current position of the word_count counter
				current_word = words[len_count].lower()
				# Loop through the words again seeing is certain conditions are met.
				for word in words:
						word = word.lower()
						if (current_word == word and current_word != 'and' and current_word != 'the' and current_word != 'The'
						and current_word != 'on' and current_word != 'of' and current_word != 'But' and current_word != 'from' and current_word != 'any'
						and current_word != 'nor' and current_word != 'this' and current_word != 'is' and current_word != 'by' and current_word != 'it'
						and current_word != 'take' and current_word != 'that' and current_word != 'but' and current_word != 'for'
						and current_word != 'these' and current_word != 'can' and current_word != 'or' and current_word != 'are'
						and current_word != 'did' and current_word != 'who' and current_word != 'say' and current_word != 'It'
						and current_word != 'rather' and current_word != 'in' and current_word != 'thus' and current_word != 'as'
						and current_word != 'do' and current_word != 'so' and current_word != 'will' and current_word != 'a'
						and current_word != 'not' and current_word != 'here' and current_word != 'whether' and current_word != 'Now'
						and current_word != 'altogether' and current_word != 'which' and current_word != 'to' and current_word != 'met'
						and current_word != 'what' and current_word != 'those' and current_word != 'always' and current_word != 'So'
						and current_word != 'Again' and current_word != 'And' and current_word != 'As' and current_word != 'Go'
						and current_word != 'well' and current_word != 'have' and current_word != 'has' and current_word != 'all'
						and current_word != 'must' and current_word != 'i' and current_word != 'my' and current_word != 'like'
						and current_word != 'me' and current_word != 'now' and current_word != 'shall' and current_word != 'with'
						and current_word != 'ever' and current_word != 'also' and current_word != 'be' and current_word != 'more'
						and current_word != 'upon' and current_word != 'no' and current_word != 'most' and current_word != 'could'
						and current_word != 'should' and current_word != 'come' and current_word != 'during' and current_word != 'been'
						and current_word != 'among' and current_word != 'toward' and current_word != 'there' and current_word != 'only'
						and current_word != 'become' and current_word != 'may' and current_word != 'need' and current_word != 'between'
						and current_word != 'every' and current_word != 'other' and current_word != 'yet' and current_word != 'let'
						and current_word != 'into' and current_word != 'about' and current_word != 'know' and current_word != 'was'
						and current_word != 'going' and current_word != 'very'  and current_word != 'it.s' and current_word != 'tell'
						and current_word != 'they.re' and current_word != 'because' and current_word != 'want' and current_word != 'never'
						and current_word != 'them' and current_word != 'many'  and current_word != 'just' and current_word != 'don.t'
						and current_word != 'big' and current_word != 'when'  and current_word != 'it.' and current_word != 'your'
						and current_word != 'said,' and current_word != 'he'  and current_word != 'way,' and current_word != 'we.ve'
						and current_word != 'back' and current_word != 'that.s'  and current_word != 'at' and current_word != 'we.re'
						and current_word != 'over' and current_word != 'new'  and current_word != 'i.ve' and current_word != 'got'
						and current_word != 'look' and current_word != 'what.s' and current_word != 'were' and current_word != '\x19s'
						and current_word != '' and current_word != '\x19re' and current_word != '(applause.)' and current_word != '\x14'
						and current_word != 'an' and current_word != '\x14' and current_word != 'make' and current_word != 'bring'
						and current_word != 'much' and current_word != 'get' and current_word != 'than' and current_word != 'even'
						and current_word != 'think' and current_word != 'really' and current_word != 'right' and current_word != 't'
						and current_word != 'remember' and current_word != 'up' and current_word != 'didn.t' and current_word != 'right.'
						and current_word != 'know,' and current_word != 'folks.' and current_word != 'go' and current_word != 'see'
						and current_word != 'lot' and current_word != 'out' and current_word != 'if' and current_word != 'had'
						and current_word != 'audience' and current_word != '[laughter]' and current_word != 'both' and current_word != 'something'
						and current_word != 'mr.' and current_word != 'that’s' and current_word != 'it’s' and current_word != 'doing'
						and current_word != '(applause)' and current_word != 'better' and current_word != 'way' and current_word != "we're"
						and current_word != '—' and current_word != 'said' and current_word != '(applause' and current_word != 'today'
						and current_word != '\x19t' and current_word != 'lower' and current_word != 'percent' and current_word != 'again'
						and current_word != 'long' and current_word != 'time' and current_word != 'tonight' and current_word != 'its'
						and current_word != 'am' and current_word != '\x19ve' and current_word != 'his' and current_word != '--'
						and current_word != '(laughter' and current_word != 'don’t' and current_word != 'some' and current_word != 'we’re'
						and current_word != 'where' and current_word != 'would' and current_word != 'under'):
								word_count += 1
								if (word_count >= times_word_appears):
										word_and_count[current_word] = word_count
				len_count += 1
		return word_and_count
	
	def buildChartData(self, word_and_count, words):
		word_count_chart_data = []
		columns = ['Word', 'Count']
		word_count_chart_data.append(columns)
		for word, count in word_and_count.items():
				rows = []
				rows.append(word)
				rows.append(count)
				word_count_chart_data.append(rows)
		if len(word_count_chart_data) == 1:
			word_and_count = self.clean_word_list(words, 2)
			word_count_chart_data = self.buildChartData(word_and_count, words)
		return word_count_chart_data
