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
		index = 0
		for column in data_file.columns:
			columns = {}
			columns['index'] = index
			columns['name'] = column
			column_names.append(columns)
			index += 1
		return column_names
	
	# def get_data_types(self, data_file):
	# 	data_types = []
	# 	count = 0
	# 	for column in data_file.columns:
	# 		data_type = data_file.dtypes[count]
	# 		data_types.append(data_type.to_string())
	# 		count += 1
	# 	print(data_types)
		# return column_names_and_data_types