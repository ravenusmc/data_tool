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

    # Keeping this here for future reference...
    # def get_list_total(self, value):
    #     return sum(int(v) for v in value[1:])

    def get_needed_values_from_data(self, graph_data):
        return graph_data[0:9]

    def sort_graph_data(self, graph_data):
        column_names = graph_data.pop(0)
        graph_data = sorted(graph_data, key=lambda value: sum(v
                                                              for v in value[1:]), reverse=True)
        graph_data.insert(0, column_names)
        graph_data = self.get_needed_values_from_data(graph_data)
        return graph_data
