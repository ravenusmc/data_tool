# This file will handle helper methods for the Data class 

# importing supporting libraries
import numpy as np
import pandas as pd

class Data_Helper():

		def get_unique_values_x_axis(self, data_file, post_data):
			return data_file[post_data['payload']['xAxisValue']].unique()
