# This file will handle helper methods for the Data class

# importing supporting libraries
import numpy as np
import pandas as pd


class Data_Helper():

	def get_unique_values_x_axis(self, data_file, post_data):
		return data_file[post_data['payload']['xAxisValue']].unique()

	def get_unique_values_y_axis(self, data_file, post_data):
		return data_file[post_data['payload']['yAxisValue']].unique()

	def get_length_unique_values(self, unique_values):
		return len(unique_values)

	def get_list_total(self, value):
		current_value_sum = 0
		for v in value[1:]:
			if isinstance(v, int):
				v = int(v)
				current_value_sum = v + current_value_sum
		return current_value_sum

	def sort_graph_data(self, graph_data):
		outer_loop_count = 1
		for value in graph_data[1:]:
			current_data_list = value
			current_value_sum_first = self.get_list_total(value)
			inner_loop_count = 2
			for v in graph_data[2:]:
				current_value_sum_second = self.get_list_total(v)
				if current_value_sum_first > current_value_sum_second:
					graph_data[outer_loop_count], graph_data[current_value_sum_second] = graph_data[
						current_value_sum_second], graph_data[outer_loop_count]
		print(graph_data)

