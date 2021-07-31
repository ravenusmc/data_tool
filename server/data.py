# This file will deal with the data analysis part of the application 

# importing supporting libraries
import numpy as np
import pandas as pd

# Importing files that I created for the project
from data_helper import *

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
	
	def get_column_data_for_graph(self, data_file, post_data, unique_values):
		x_axis_column = post_data['payload']['xAxisValue']
		data_helper_obj = Data_Helper()
		graph_data = []
		columns = [post_data['payload']['xAxisValue'], post_data['payload']['yAxisValue']]
		graph_data.append(columns)
		for unique_value in unique_values:
			rows = []
			count = int(len(data_file[(data_file[x_axis_column] == unique_value)]))
			rows.append(unique_value)
			rows.append(count)
			graph_data.append(rows)
		return graph_data
		# Need to handle if there are to many unique values - let user know best not to 
		# use that column 
		# Need to get unique values of x-axis. 
		# Handle situation when dealing with dates - Have a check when submitting axis names? 
		# dataset_length = len(new_data_set[(new_data_set.category == category) & (new_data_set.state == 'successful')])
	
