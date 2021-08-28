def build_data_graph():
    if request.method == 'POST':
        data_helper_obj = Data_Helper()
        data_graph_information = {}
        post_data = request.get_json()
        data_object = Data(post_data['payload']['fileName'])
        data_file = data_object.getting_data_file()
        # Checking for Unique Values - x axis
        unique_values = data_helper_obj.get_unique_values_x_axis(
            data_file, post_data)
        unique_values_length_x_axis = data_helper_obj.get_length_unique_values(
            unique_values)
        # Checking for unique Values - y axis
        unique_values_y_axis = data_helper_obj.get_unique_values_y_axis(
            data_file, post_data)
        # Getting graph data
        graph_data = data_object.get_column_data_for_graph(
            data_file, post_data, unique_values)
        column_names = graph_data.pop(0)
        graph_data = sorted(graph_data, key=lambda x: x[1], reverse=True)
        graph_data.insert(0, column_names)
        graph_data = graph_data[0:4]
        print(graph_data)
        input()
        if unique_values_length_x_axis > 8:
            if post_data['payload']['aggregateValue']:
                graph_data = data_object.get_column_data_for_graph_aggregate(
                    data_file, post_data, unique_values, unique_values_y_axis)
                graph_data = data_helper_obj.sort_graph_data(graph_data)
                data_graph_information['graph_data'] = graph_data
                data_graph_information['show_user_warning'] = False
                data_graph_information['show_graph'] = True
                data_graph_information['show_chart_controls'] = True
            else:
                data_graph_information['show_user_warning'] = True
        else:
            if post_data['payload']['uniqueValue'] == 'true':
                unique_values_y_axis = data_helper_obj.get_unique_values_y_axis(
                    data_file, post_data)
                graph_data = data_object.get_column_data_for_graph_unique_y_values(
                    data_file, post_data, unique_values, unique_values_y_axis)
            else:
                graph_data = data_object.get_column_data_for_graph(
                    data_file, post_data, unique_values)
            data_graph_information['show_user_warning'] = False
            data_graph_information['graph_data'] = graph_data
            data_graph_information['show_graph'] = True
            data_graph_information['show_chart_controls'] = True
        return jsonify(data_graph_information)