# This file will deal with building the data graph part of the application 

# importing supporting libraries
import numpy as np
import pandas as pd

class Graph_Data():
	
	def get_column_data_for_graph(self, post_data):
		graph_data = []
		columns = [post_data['payload']['xAxisValue'], post_data['payload']['yAxisValue']]
		graph_data.append(columns)
