# This file will deal with the data analysis part of the application 

# importing supporting libraries
import numpy as np
import pandas as pd

class Data():

	def __init__(self, file_name):
		self.file_name = file_name
	
	def getting_data_file(self):
		return pd.read_csv('./data/' + self.file_name)
	
	def get_column_names(self, data_file):
		column_names = []
		for column in data_file.columns:
			column_names.append(column)
		return column_names