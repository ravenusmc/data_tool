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

    def get_data_types(self, data_file):
        print(data_file)

    def get_column_data_for_graph(self, data_file, post_data, unique_values):
        x_axis_column = post_data['payload']['xAxisValue']
        data_helper_obj = Data_Helper()
        graph_data = []
        columns = [post_data['payload']['xAxisValue'],
                   post_data['payload']['yAxisValue']]
        graph_data.append(columns)
        for unique_value in unique_values:
            rows = []
            count = int(
                len(data_file[(data_file[x_axis_column] == unique_value)]))
            rows.append(unique_value)
            rows.append(count)
            graph_data.append(rows)
        return graph_data

    def get_column_data_for_graph_unique_y_values(self, data_file, post_data, unique_values, unique_values_y_axis):
        x_axis_column = post_data['payload']['xAxisValue']
        y_axis_column = post_data['payload']['yAxisValue']
        graph_data = []
        graph_data.append([post_data['payload']['xAxisValue'],
                           post_data['payload']['yAxisValue']])
        for unique_value in unique_values:
            rows = []
            x_axis_unique_data_data_frame = data_file[(
                data_file[x_axis_column] == unique_value)]
            total_unique_values = 0
            for uniq_value in unique_values_y_axis:
                total_unique_values = int(len(x_axis_unique_data_data_frame[(
                    x_axis_unique_data_data_frame[y_axis_column] == uniq_value)])) + total_unique_values
            rows.append(unique_value)
            rows.append(total_unique_values)
            graph_data.append(rows)
        return graph_data

    def get_column_data_for_graph_aggregate(self, data_file, post_data, unique_values_x, unique_values_y_axis):
        x_axis_column = post_data['payload']['xAxisValue']
        y_axis_column = post_data['payload']['yAxisValue']
        graph_data = []
        header_row = []
        header_row.append(x_axis_column)
        for value in unique_values_y_axis:
            header_row.append(value)
        graph_data.append(header_row)
        for unique_value in unique_values_x:
            x_axis_unique_data_data_frame = data_file[(
                data_file[x_axis_column] == unique_value)]
            rows = []
            rows.append(unique_value)
            y_axis_count_data = x_axis_unique_data_data_frame.groupby(
                [y_axis_column]).count()
            count_values_list = []
            for uniq_value in unique_values_y_axis:
                unique_values_y_count = int(len(x_axis_unique_data_data_frame[(
                    x_axis_unique_data_data_frame[y_axis_column] == uniq_value)]))
                count_values_list.append(unique_values_y_count)
            rows = rows + count_values_list
            graph_data.append(rows)
        return graph_data
