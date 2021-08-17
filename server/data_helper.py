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
            v = int(v)
            current_value_sum = v + current_value_sum
        return current_value_sum

    # def sort_graph_data(self, graph_data):
    #     count = 1
    #     for value in graph_data[1:]:
    #         current_data_list = value
    #         current_value_sum_first = self.get_list_total(value)
    #         for v in graph_data[2:]:
    #             current_value_sum_second = self.get_list_total(v)
    #             if current_value_sum_first > current_value_sum_second:
    #                 # print(count)
    #                 # print(graph_data[count])
    #                 graph_data[count], graph_data[count +
    #                 1] = graph_data[count + 1], graph_data[count]
    #                 # print(graph_data[1:5])
    #             # input()
    #         count += 1
    #     print(graph_data)

    def sort_graph_data(self, graph_data):
        column_names = graph_data.pop(0)
        n = len(graph_data)
        for i in range(n-1):
            current_value_sum_first = self.get_list_total(graph_data[i])
            for j in range(0, n-i-1):
                current_value_sum_second = self.get_list_total(
                    graph_data[j + 1])
                if current_value_sum_first > current_value_sum_second:
                    print(current_value_sum_first)
                    print(current_value_sum_second)
                    print(graph_data[0:5])
                    graph_data[j], graph_data[j +
                                              1] = graph_data[j + 1], graph_data[j]
                    print('------------')
                    print(graph_data[0:5])
                    input()
        print(graph_data)
