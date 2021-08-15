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

    def sort_graph_data(self, graph_data):
        # print(type(graph_data))
        for value in graph_data[1:]:
			current_data_list = value
            current_value_sum = 0
            for v in value[1:]:
                v = int(v)
                current_value_sum = v + current_value_sum
            print(value)
            print(current_value_sum)
            input()
