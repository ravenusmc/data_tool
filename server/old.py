<div >
        <h6 > Pick Chart Type: < /h6 >
        <input
          @change = "graphTypeSelected()"
          type = "radio"
          id = "one"
          value = "BarChart"
          v-model = "graphType"
        / >
        <label for = "one" > Bar Chart < /label >
        <br / >
        <div v-if = "hideControlsBasedOnAggregateValueSelected" >
          <input
            @change = "graphTypeSelected()"
            type = "radio"
            id = "two"
            value = "PieChart"
            v-model = "graphType"
          / >
          <label for = "two" > Pie Chart < /label >
        </div >
        <br / >
        <input
          @change = "graphTypeSelected()"
          type = "radio"
          id = "two"
          value = "ColumnChart"
          v-model = "graphType"
        / >

        <label for = "two" > Column Chart < /label >
      </div>
      <!-- End chart type div -->
      <!-- unique values div -->
      <div>
        <h6>Unique Values: (Y - Axis)</h6>
        <input
          @change="uniqueValueSelected()"
          type="radio"
          id="one"
          value="true"
          v-model="uniqueValue"
        />
        <label for="one">Unique Values - Y Axis</label>
        <br />
        <input
          @change="uniqueValueSelected()"
          type="radio"
          id="two"
          value="False"
          v-model="uniqueValue"
        />
        <label for="two">All Values - Y Axis</label>
      </div>
      <!-- End unique values div -->
      <!-- Aggregate div -->
      <div>
        <h6>Use Aggregate Value</h6>
        <input
          @change="aggregateValueSelected()"
          type="checkbox"
          id="checkbox"
          value="true"
          v-model="aggregateValueChecked"
        />
        <label for="checkbox">Aggregate Value Y Axis</label>
      </div>



# else:
#     data_graph_information['show_user_warning'] = True
# else:
#     if post_data['payload']['uniqueValue'] == 'true':
#         unique_values_y_axis = data_helper_obj.get_unique_values_y_axis(
#             data_file, post_data)
#         graph_data = data_object.get_column_data_for_graph_unique_y_values(
#             data_file, post_data, unique_values, unique_values_y_axis)
#     else:
#         graph_data = data_object.get_column_data_for_graph(
#             data_file, post_data, unique_values)
#     data_graph_information['show_user_warning'] = False
#     data_graph_information['graph_data'] = graph_data
#     data_graph_information['show_graph'] = True
#     data_graph_information['show_chart_controls'] = True


682

Working:
Console.log:
{graph_data: Array(3), show_chart_controls: true,
 show_graph: true, show_user_warning: false}

print:
{'show_user_warning': False, 'graph_data': [['type', 'show_id'], ['Movie', 5377], [
    'TV Show', 2410]], 'show_graph': True, 'show_chart_controls': True}

Not working:

print:
{'show_user_warning': True, 'graph_data': [['country', 'type'], ['United States', 2555], ['India', 923],
                                           ['United Kingdom', 397], [
                                               'Japan', 226], ['South Korea', 183],
                                           ['Canada', 177], ['Spain', 134], [
                                               'France', 115], ['Egypt', 101],
                                           ['Mexico', 100], ['Turkey', 100], ['Australia', 83], ['Taiwan', 78], ['Brazil', 72], ['Philippines', 71], ['Nigeria', 70], ['Indonesia', 70], ['United Kingdom, United States', 64], ['Germany', 61], ['United States, Canada', 60], ['Thailand', 57], ['China', 57], ['Hong Kong', 52], ['Argentina', 50], ['Canada, United States', 42], ['Italy', 40], ['United States, United Kingdom', 37], ['Colombia', 31], ['France, Belgium', 27], ['South Africa', 25], ['Singapore', 23], ['Malaysia', 22], ['Poland', 20], ['Pakistan', 18], ['Netherlands', 16], ['Russia', 16], ['Hong Kong, China', 16], ['Mexico, United States', 14], ['China, Hong Kong', 14], ['Lebanon', 14], ['Chile', 14], ['United States, France', 14], ['Denmark', 13], ['United States, Japan', 13], ['United States, Germany', 12], ['United Arab Emirates', 12], ['Israel', 12], ['United States, Mexico', 11], ['Norway', 11], ['United States, Australia', 11], ['New Zealand', 11], ['Ireland', 11], ['Australia, United States', 10], ['Germany, United States', 10], ['Sweden', 10], ['Japan, United States', 9], ['India, United States', 9], ['United States, India', 8], ['Argentina, Spain', 8], ['Belgium', 8], ['United States, China', 7], ['Saudi Arabia', 7], ['Romania', 6], ['United States, France, Japan', 6], ['United Kingdom, France', 6], ['Kuwait', 6], ['United Kingdom, Canada, United States', 6], ['France, United States', 6], ['United States, Italy', 5], ['Vietnam', 5], ['India, France', 5], ['Spain, France', 5], ['Italy, France', 5], ['South Korea, United States', 5], ['United States, Czech Republic', 5], ['Poland, United States', 4], ['Iceland', 4], ['South Africa, United States', 4], ['Peru', 4], ['United States, United Kingdom, Australia', 4], ['United Kingdom, Canada', 4], ['Hungary', 4], ['United Kingdom, Japan, United States', 4], ['Hong Kong, United States', 4], ['United Kingdom, United States, Spain, Germany, Greece, Canada', 4], ['Austria', 4], ['United Kingdom, France, United States', 4], ['United States, Spain', 4], ['United Kingdom, Germany', 4], ['Mexico, Spain', 4], ['United States, South Africa', 3], ['United States, United Kingdom, France', 3], ['Israel, United States', 3], ['Bulgaria, United States', 3], ['United States, Bulgaria', 3], ['France, Egypt', 3], ['Uruguay', 3], ['Sweden, United States', 3], ['Denmark, United States', 3], ['Ghana', 3], ['Belgium, France', 3], ['United States, Sweden', 3], ['Canada, United States, United Kingdom', 3], ['France, United Kingdom, United States', 3], ['United States, United Arab Emirates', 3], ['United States, Ireland', 3], ['France, Canada', 3], ['United States, Russia', 3], ['Spain, Germany', 3], ['Italy, United States', 3], ['United States, New Zealand', 3], ['United States, Hong Kong', 3], ['Kenya', 2], ['France, South Korea, Japan', 2], ['United Arab Emirates, United States', 2], ['Turkey, United States', 2], ['United States, Chile', 2], ['Ireland, United Kingdom, United States', 2], ['Spain, Italy', 2], ['United States, Germany, Canada', 2], ['Serbia, United States', 2], ['India, Germany', 2], ['Singapore, United States', 2], ['Australia, Canada', 2], ['United Kingdom, Ireland', 2], ['Ireland, United Kingdom', 2], ['Canada, United Kingdom', 2], ['Indonesia, Singapore', 2], ['United Kingdom, United States, Australia', 2], ['China, United States', 2], ['United Kingdom, India', 2], ['United States, South Korea, China', 2], ['Czech Republic, United States', 2], ['Brazil, France', 2], ['Thailand, United States', 2], ['Netherlands, Belgium', 2], ['Hong Kong, China, United States', 2], ['United States, Canada, United Kingdom', 2], ['Canada, United States, France', 2], ['United States, United Kingdom, Germany', 2], ['Spain, United Kingdom', 2], ['Bangladesh', 2], ['United States, Japan, Canada', 2], ['United States, Argentina', 2], ['Colombia, Mexico, United States', 2], ['United Kingdom, Italy', 2], ['Germany, United Kingdom', 2], ['United States, Greece', 2], ['China, Canada, United States', 2], ['Pakistan, United States', 2], ['Australia, United Arab Emirates', 2], ['Canada, India', 2], ['Ukraine', 2], ['India, Soviet Union', 2], ['Canada, United Kingdom, United States', 2], ['Switzerland', 2], ['Spain, Argentina', 2], ['United Kingdom, India, United States', 2], ['Spain, Mexico', 2], ['Canada, Australia', 2], ['Egypt, France', 2], ['New Zealand, United States', 2], ['United Kingdom, Nigeria', 2], ['Lebanon, Canada, France', 2], ['Norway, Iceland, United States', 1], ['South Africa, Nigeria', 1], ['Portugal, Spain', 1], ['Hong Kong, China, Singapore', 1], ['South Africa, China, United States', 1], ['United States, France, Serbia', 1], ['Denmark, France, Poland', 1], ['New Zealand, United Kingdom', 1], ['Netherlands, Denmark, South Africa', 1], ['France, Netherlands, Singapore', 1], ['United Kingdom, Spain, United States', 1], ['United Kingdom, Hong Kong', 1], ['Iran, France', 1], ['United Kingdom, France, Belgium, United States, China', 1], ['Argentina, Brazil, France, Poland, Germany, Denmark', 1], ['Uruguay, Argentina, Spain', 1], ['Singapore, France', 1], ['United Kingdom, United States, France, Germany', 1], ['Australia, France', 1], ['Hong Kong, Iceland, United States', 1], ['Germany, France, Russia', 1], ['Mauritius, South Africa', 1], ['Uruguay, Argentina', 1], ['Egypt, Algeria', 1], ['Soviet Union, India', 1], ['United Kingdom, France, Germany', 1], ['Canada, Luxembourg', 1], ['Canada, Nigeria', 1], ['Iceland, Sweden, Belgium', 1], ['Ireland, Canada', 1], ['Finland', 1], ['China, Spain, South Korea, United States', 1], ['Spain, Belgium', 1], ['United Kingdom, Canada, United States, Germany', 1], ['Brazil, Netherlands, United States, Colombia, Austria, Germany', 1], ['France, Canada, Belgium', 1], ['India, United Kingdom, China, Canada, Japan, South Korea, United States', 1], ['Indonesia, South Korea, Singapore', 1], ['France, Senegal, Belgium', 1], ['Canada, France', 1], ['Romania, France, Switzerland, Germany', 1], ['Bulgaria, United States, Spain, Canada', 1], ['Sweden, Netherlands', 1], ['France, United States, Mexico', 1], ['Australia, United Kingdom, United Arab Emirates, Canada', 1], ['Japan, Canada, United States', 1], ['Australia, Armenia, Japan, Jordan, Mexico, Mongolia, New Zealand, Philippines, South Africa, Sweden, United States, Uruguay', 1], ['Norway, Denmark, Netherlands, Sweden', 1], ['Namibia', 1], ['Mexico, Finland', 1], ['Uruguay, Spain, Mexico', 1], ['South Korea, China', 1], ['United States, Canada, Indonesia, United Kingdom, China, Singapore', 1], ['India, Iran', 1], ['Turkey, India', 1], ['Philippines, Qatar', 1], ['Ireland, Luxembourg, Belgium', 1], ['Saudi Arabia, Syria, Egypt, Lebanon, Kuwait', 1], ['Russia, United States', 1], ['United Kingdom, Russia, United States', 1], ['Germany, Jordan, Netherlands', 1], ['Argentina, United States', 1], ['France, Belgium, Spain', 1], ['Denmark, Sweden, Israel, United States', 1], ['United States, Iceland', 1], ['United Arab Emirates, United Kingdom, India', 1], ['Norway, Germany, Sweden', 1], ['Finland, France', 1], ['Denmark, Spain', 1], ['United Kingdom, Russia', 1], ['India, United Kingdom', 1], ['United States, Canada, Ireland', 1], ['United States, Israel, Italy, South Africa', 1], ['United Kingdom, China', 1], ['Netherlands, Denmark, France, Germany', 1], ['South Korea, Japan', 1], ['Philippines, Canada, United Kingdom, United States', 1], ['France, Malta, United States', 1], ['United Kingdom, Pakistan', 1], ['France, New Zealand', 1], ['United Kingdom, Czech Republic, United States, Germany, Bahamas', 1], ['United States, Australia, China', 1], ['China, Germany, India, United States', 1], ['Germany, Sri Lanka', 1], ['Canada, United States, Cayman Islands', 1], ['United States, India, Bangladesh', 1], ['United States, Canada, France', 1], ['Taiwan, China, France, United States', 1], ['Brazil, France, Germany', 1], ['United States,', 1], ['Turkey, France, Germany, Poland', 1], ['Australia, New Zealand, United States', 1], ['Germany, United States, Hong Kong, Singapore', 1], ['France, Germany, Switzerland', 1], ['Mexico, Argentina', 1], ['Italy, United States, Argentina', 1], ['Germany, France, Luxembourg, United Kingdom, United States', 1], ['United Kingdom, Canada, Italy', 1], ['Czech Republic, France', 1], ['Zimbabwe', 1], ['United Kingdom, France, Germany, Spain', 1], ['Taiwan, Hong Kong, United States, China', 1], ['Canada, Brazil', 1], ['United Kingdom, Australia', 1], ['Germany, Australia', 1], ['United Kingdom, Poland, United States', 1], ['Bulgaria', 1], ['Philippines, United States', 1], ['Finland, Germany', 1], ['United States, Thailand', 1], ['Spain, Belgium, Switzerland, United States, China, United Kingdom', 1], ['Denmark, Zimbabwe', 1], ['United Kingdom, South Africa', 1], ['Finland, Sweden, Norway, Latvia, Germany', 1], ['South Africa, United States, New Zealand, Canada', 1], ['France, Qatar', 1], ['France, Algeria', 1], ['United States, Italy, United Kingdom, Liechtenstein', 1], ['Denmark, France, Belgium, Italy, Netherlands, United States, United Kingdom', 1], ['United States, Australia, Mexico', 1], ['United Kingdom, Czech Republic, Germany, United States', 1], ['Russia, Poland, Serbia', 1], ['France, China, Japan, United States', 1], ['Germany, Belgium', 1], ['Chile, Argentina', 1], ['China, United States, United Kingdom', 1], ['Pakistan, Norway, United States', 1], ['Philippines, Singapore', 1], ['United States, Canada, Belgium, United Kingdom', 1], ['Venezuela', 1], ['Argentina, Uruguay, Serbia', 1], ['United States, Mexico, Colombia', 1], ['Colombia, Peru, United Kingdom', 1], ['Brazil, United States', 1], ['Canada, France, Italy, Morocco, United States', 1], ['Canada, Spain, France', 1], ['France, Canada, China, Cambodia', 1], ['United States, Indonesia', 1], ['Spain, Mexico, France', 1], ['Spain, France, Italy', 1], ['Spain, France, United States', 1], ['United States, France, Canada', 1], ['Cambodia, United States', 1], ['China, Japan', 1], ['United Arab Emirates, United States, United Kingdom', 1], ['Argentina, Italy', 1], ['United Kingdom, Israel, Russia', 1], ['Italy, Switzerland, Albania, Poland', 1], ['Spain, Cuba', 1], ['United States, Brazil', 1], ['United States, France, Mexico', 1], ['United States, Nicaragua', 1], ['Austria, Germany', 1], ['United Arab Emirates, Jordan, Lebanon', 1], ['France, Belgium, Luxembourg, Cambodia,', 1], ['Italy, Turkey', 1], ['India, Turkey', 1], ['Kenya, United States', 1], ['United States, South Korea', 1], ['Italy, Canada, France', 1], ['United Kingdom, Denmark, Canada, Croatia', 1], ['United Kingdom, Canada, United States, Cayman Islands', 1], ['Italy, Germany', 1], ['United States, France, United Kingdom, Japan', 1], ['United States, United Kingdom, Denmark, Sweden', 1], ['United States, United Kingdom, Italy', 1], ['United States, France, Canada, Spain', 1], ['Uruguay, Guatemala', 1], ['Germany, Australia, France, China', 1], ['United States, United Kingdom, Japan', 1], ['United States, United Kingdom, Canada', 1], ['Italy, Switzerland, France, Germany', 1], ['Russia, United States, China', 1], ['United States, Canada, Germany', 1], ['Ireland, United States', 1], ['France, Australia, Germany', 1], ['Lebanon, United Arab Emirates, France, Switzerland, Germany', 1], ['United States, South Korea, Japan', 1], ['Romania, United States', 1], ['West Germany', 1], ['Chile, Italy', 1], ['Ireland, United Kingdom, Italy, United States', 1], ['Poland,', 1], ['Slovenia, Croatia, Germany, Czech Republic, Qatar', 1], ['Canada, United Kingdom, Netherlands', 1], ['United Kingdom, United States, France', 1], ['Indonesia, United Kingdom', 1], ['United States, Spain, Germany', 1], ['India, Japan', 1], ['Switzerland, France, Belgium, United States', 1], ['China, South Korea, United States', 1], ['United Kingdom, France, Belgium', 1], ['Canada, Ireland, United States', 1], ['United Kingdom, United States, Dominican Republic', 1], ['United States, Senegal', 1], ['Germany, United Kingdom, United States', 1], ['United Kingdom, Germany, Canada', 1], ['Argentina, France', 1], ['South Africa, Germany, Netherlands, France', 1], ['Canada, United States, United Kingdom, France, Luxembourg', 1], ['Finland, Germany, Belgium', 1], ['Taiwan, China', 1], ['Cambodia', 1], ['Spain, Portugal', 1], ['Ireland, United States, France', 1], ['Jordan', 1], ['Germany, United States, Canada', 1], ['United Kingdom, Germany, Canada, United States', 1], [
    'United States, France, Canada, Lebanon, Qatar', 1], ['Indonesia, Netherlands', 1], ['Netherlands, Belgium, United Kingdom, United States', 1], ['China, United States, Australia', 1], ['France, Belgium, China, United States', 1], ['United States, Chile, Israel', 1], ['United Kingdom, Norway, Denmark, Germany, Sweden', 1], ['Norway, Denmark, Sweden', 1], ['China, India, Nepal', 1], ['Mexico, United States, Spain, Colombia', 1], ['United Kingdom, Belgium, Sweden', 1], ['Nigeria, United Kingdom', 1], ['United Kingdom, South Korea', 1], ['United States, Taiwan', 1], ['Netherlands, Belgium, Germany, Jordan', 1], ['Denmark, Singapore, Canada, United States', 1], ['Denmark, China', 1], ['Malaysia, Singapore, Hong Kong', 1], ['Norway, United States', 1], ['United States, Philippines', 1], ['United States, Greece, Brazil', 1], ['South Korea, France', 1], ['United States, Australia, Samoa, United Kingdom', 1], ['Canada, South Africa', 1], ['China, United Kingdom', 1], ['Argentina, Chile, Peru', 1], ['Uruguay, Germany', 1], ['Turkey, Azerbaijan', 1], ['United States, China, Hong Kong', 1], ['Canada, Germany, France, United States', 1], ['Argentina, United States, Mexico', 1], ['France, United Kingdom, India', 1], ['China, Taiwan', 1], ['Italy, United Kingdom, France', 1], ['Poland, West Germany', 1], ['Germany, United States, Sweden', 1], ['Canada, Spain', 1], ['United Kingdom, France, Belgium, United States', 1], ['France, Japan', 1], ['Netherlands, Germany, Italy, Canada', 1], ['United States, Cambodia', 1], ['United States, China, Colombia', 1], ['United States, Spain, Italy', 1], ['Norway, United Kingdom, France, Ireland', 1], ['United States, Bermuda, Ecuador', 1], ['United Kingdom, Poland', 1], ['India, Mexico', 1], ['United Kingdom, West Germany', 1], ['Israel, Sweden, Germany, Netherlands', 1], ['Chile, United States, France', 1], ['France, Morocco', 1], ['Georgia, Germany, France', 1], ['Switzerland, France', 1], ['Turkey, South Korea', 1], ['Italy, India', 1], ['United States, Botswana', 1], ['United States, Colombia, Mexico', 1], ['Chile, Argentina, France, Spain, United States', 1], ['Puerto Rico, United States, Colombia', 1], ['United States, Nigeria', 1], ['Germany, United States, France', 1], ['Spain, Germany, Denmark, United States', 1], ['United Kingdom, United States, Japan', 1], ['Netherlands, United States', 1], ['United States, India, South Korea, China', 1], ['Denmark, Germany, Belgium, United Kingdom, France', 1], ['Denmark, Germany, Belgium, United Kingdom, France, Sweden', 1], ['France, Switzerland, Spain, United States, United Arab Emirates', 1], ['Norway, Sweden', 1], ['United States, Ireland, United Kingdom, India', 1], ['United Kingdom, Singapore', 1], ['Germany, Czech Republic', 1], ['Denmark, Brazil, France, Portugal, Sweden', 1], ['Brazil, India, China, United States', 1], ['India, Germany, Austria', 1], ['Denmark, France, United States, Sweden', 1], ['Australia, Iraq', 1], ['China, Morocco, Hong Kong', 1], ['Spain, Colombia', 1], ['Canada, United States, Germany', 1], ['France, Belgium, Italy', 1], ['United Kingdom, Thailand', 1], ['Venezuela, Colombia', 1], ['France, Luxembourg, Canada', 1], ['India, Nepal', 1], ['Colombia, United States', 1], ['Colombia, Mexico', 1], ['France, Germany, Czech Republic, Belgium', 1], ['Germany, China, United Kingdom', 1], ['Canada, Hungary, United States', 1], ['Pakistan, United Arab Emirates', 1], ['France, United Kingdom', 1], ['Spain, United Kingdom, United States', 1], ['United Kingdom, Kenya', 1], ['United States, Norway, Canada', 1], ['Canada, United States, Ireland', 1], ['Switzerland, Vatican City, Italy, Germany, France', 1], ['Portugal, France, Poland, United States', 1], ['France, Japan, United States', 1], ['United States, New Zealand, Japan', 1], ['United States, Netherlands, Japan, France', 1], ['India, Switzerland', 1], ['Canada, Japan, United States', 1], ['United States, Morocco', 1], ['United States, Mexico, Spain, Malta', 1], ['Norway, Denmark', 1], ['South Korea, Canada, United States, China', 1], ['Singapore, Japan, France', 1], ['Canada, Mexico, Germany, South Africa', 1], ['United Kingdom, United States, Canada', 1], ['Germany, France, United States, Canada, United Kingdom', 1], ['Peru, Germany, Norway', 1], ['Singapore, Malaysia', 1], ['United States, Uruguay', 1], ['India, Canada', 1], ['Ireland, Canada, United Kingdom, United States', 1], ['United States, Germany, Australia', 1], ['Senegal', 1], ['Israel, Germany, France', 1], ['Australia, France, Ireland', 1], ['South Africa, Angola', 1], ['Austria, Czech Republic', 1], ['Australia, India', 1], ['United States, United Kingdom, Canada, Japan', 1], ['Sweden, United Kingdom, Finland', 1], ['Hong Kong, Taiwan', 1], ['United States, United Kingdom, Spain, South Korea', 1], ['South Korea, China, United States', 1], ['Guatemala', 1], ['United States, United Kingdom, Canada, China', 1], ['Italy, South Africa, West Germany, Australia, United States', 1], ['United Kingdom, Finland, Germany', 1], ['South Africa, United States, Germany', 1], ['United States, Germany, United Kingdom, Australia', 1], ['Italy, France, Switzerland', 1], ['Canada, France, United States', 1], ['United States, Colombia', 1], ['India, Malaysia', 1], ['Switzerland, United States', 1], ['Thailand, Canada, United States', 1], ['China, Hong Kong, United States', 1], ['United Kingdom, New Zealand', 1], ['United Kingdom, France, Germany, United States', 1], ['South Korea, Czech Republic', 1], ['Czech Republic, United Kingdom, France', 1], ['Australia, United Kingdom, Canada', 1], ['United States, Hungary', 1], ['Jamaica, United States', 1], ['Australia, United Kingdom, United States, New Zealand, Italy, France', 1], ['France, United States, Canada', 1], ['Australia, United Kingdom', 1], ['United States, Denmark', 1], ['United Kingdom, France, Canada, Belgium, United States', 1], ['Denmark, United Kingdom, Sweden', 1], ['Belarus', 1], ['Cyprus', 1], ['Lebanon, United States, United Arab Emirates', 1], ['United States, Kazakhstan', 1], ['Argentina, France, United States, Germany, Qatar', 1], ['United States, Germany, United Kingdom', 1], ['United States, Germany, United Kingdom, Italy', 1], ['United States, New Zealand, United Kingdom', 1], ['Finland, United States', 1], ['Spain, France, Uruguay', 1], ['France, Belgium, United States', 1], ['France, Canada, United States', 1], ['Chile, France', 1], ['United States, United Kingdom, France, Germany, Japan', 1], ['Canada, Norway', 1], ['United States, Hungary, Ireland, Canada', 1], ['United States, Canada, China', 1], ['United Kingdom, Malawi', 1], ['Ireland, Canada, Luxembourg, United States, United Kingdom, Philippines, India', 1], ['United States, Czech Republic, United Kingdom', 1], ['Ghana, United States', 1], ['Israel, Germany', 1], ['Mexico, France', 1], ['Brazil, United Kingdom', 1], ['France, Belgium, Luxembourg, Romania, Canada, United States', 1], ['Israel, Germany, Poland, Luxembourg, Belgium, France, United States', 1], ['France, Germany', 1], ['United States, Malta, France, United Kingdom', 1], ['United Kingdom, United States, Germany, Denmark, Belgium, Japan', 1], ['Austria, United States', 1], ['Greece, United States', 1], ['United Kingdom, France, Belgium, Canada, United States', 1], ['Argentina, Chile', 1], ['Czech Republic, Slovakia', 1], ['United Kingdom, Germany, United States, France', 1], ['United Kingdom, Lithuania', 1], ['Spain, France, Canada', 1], ['United States, Greece, United Kingdom', 1], ['United Kingdom, China, United States, India', 1], ['Taiwan, Malaysia', 1], ['United States, Sweden, Norway', 1], ['United Kingdom, United States, Morocco', 1], ['United States, United Kingdom, Morocco', 1], ['United States, China, Canada', 1], ['Spain, Canada, United States', 1], ['Canada, Belgium', 1], ['United States, India, United Arab Emirates', 1], ['United Kingdom, Canada, France, United States', 1], ['Spain, Thailand, United States', 1], ['Canada, Germany, South Africa', 1], ['India, Germany, France', 1], ['United States, Israel, United Kingdom, Canada', 1], ['United Kingdom, Hungary, Australia', 1], ['Lebanon, France', 1], ['Belgium, Ireland, Netherlands, Germany, Afghanistan', 1], ['Chile, Peru', 1], ['Paraguay, Argentina', 1], ['United Kingdom, Italy, Israel, Peru, United States', 1], ['Norway, Germany', 1], ['France, Canada, Italy, United States, China', 1], ['Netherlands, Germany, Denmark, United Kingdom', 1], ['France, Lebanon', 1], ['Ireland, United Kingdom, Greece, France, Netherlands', 1], ['Denmark, Indonesia, Finland, Norway, United Kingdom, Israel, France, United States, Germany, Netherlands', 1], ['Argentina, Uruguay, Spain, France', 1], ['United Kingdom, Germany, United States', 1], ['United States, Australia, South Africa, United Kingdom', 1], ['Italy, Belgium', 1], ['United States, Germany, Mexico', 1], ['Chile, Spain, Argentina, Germany', 1], ['Germany, Italy', 1], ['Belgium, United Kingdom, United States', 1], ['Australia, New Zealand', 1], ['Spain, Switzerland', 1], ['Indonesia, United States', 1], ['Canada, South Korea, United States', 1], ['France, Iran, United States', 1], ['Croatia', 1], ['Somalia, Kenya, Sudan, South Africa, United States', 1], ['Ireland, France, Iceland, United States, Mexico, Belgium, United Kingdom, Hong Kong', 1], ['Spain, United States', 1], ['United States, Canada, Japan, Panama', 1], ['United Kingdom, Spain, Belgium', 1], ['Serbia, South Korea, Slovenia', 1], ['Denmark, United Kingdom, South Africa, Sweden, Belgium', 1], ['Germany, Canada, United States', 1], ['Ireland, South Africa', 1], ['Canada, Germany', 1], ['Spain, France, Canada, United States', 1], ['India, United Kingdom, Canada, United States', 1], ['United States, Belgium, Canada', 1], ['United States, France, Canada, Belgium', 1], ['United Kingdom, Egypt, United States', 1], ['United Kingdom, Germany, United Arab Emirates, New Zealand', 1], ['United Kingdom, France, United States, Belgium, Luxembourg, China, Germany', 1], ['United Kingdom, Spain, United States, Germany', 1], ['United States, France, Italy, United Kingdom', 1], ['Georgia', 1], ['United States, United Kingdom, India', 1], ['Ireland, Canada, United States, United Kingdom', 1], ['New Zealand, United Kingdom, Australia', 1], ['United States, Poland', 1], ['United Arab Emirates, Romania', 1], ['United Kingdom, Australia, Canada, United States', 1], ['Mexico, Netherlands', 1], ['Spain, Italy, Argentina', 1], ['Germany, United States, Italy', 1], ['United States, Venezuela', 1], ['United Kingdom, Canada, Japan', 1], ['Canada, Japan, Netherlands', 1], ['United Kingdom, United States, Czech Republic', 1], ['United Kingdom, China, United States', 1], ['United Kingdom, Brazil, Germany', 1], ['Thailand, China, United States', 1], ['United Kingdom, Namibia, South Africa, Zimbabwe, United States', 1], ['United Kingdom, South Africa, Australia, United States', 1], ['Canada, United States, India, United Kingdom', 1], ['United States, Brazil, South Korea, Mexico, Japan, Germany', 1], ['France, Lebanon, United Kingdom', 1], ['United Kingdom, Jordan, Qatar, Iran', 1], ['Switzerland, United Kingdom, United States', 1], ['Belgium, Netherlands', 1], ['United Kingdom, Germany, France, United States', 1], ['Romania, United Kingdom', 1], ['Lebanon, Qatar', 1], ['United Kingdom, India, Sweden', 1], ['United Kingdom, Belgium', 1], ['India, Pakistan', 1], ['United Kingdom,', 1], ['Saudi Arabia, Netherlands, Germany, Jordan, United Arab Emirates, United States', 1], ['France, Brazil, Spain, Belgium', 1], ['United States, Brazil, India, Uganda, China', 1], ['United Kingdom, Ireland, United States', 1], ['India, Australia', 1], ['Austria, Iraq, United States', 1], ['France, Norway, Lebanon, Belgium', 1], ['United Kingdom, France, United States, Belgium', 1], ['Saudi Arabia, United Arab Emirates', 1], ['Peru, United States, United Kingdom', 1], ['Germany, United States, United Kingdom, Canada', 1], ['Uruguay, Argentina, Germany, Spain', 1], ['France, Luxembourg, United States', 1], ['United Kingdom, Spain', 1], ['Canada, India, Thailand, United States, United Arab Emirates', 1], ['Romania, Bulgaria, Hungary', 1], ['United States, East Germany, West Germany', 1], ['France, Netherlands, South Africa, Finland', 1], ['United Kingdom, Ukraine, United States', 1], ['Egypt, Austria, United States', 1], ['Russia, Spain', 1], ['Croatia, Slovenia, Serbia, Montenegro', 1], ['Japan, Canada', 1], ['United States, France, South Korea, Indonesia', 1], ['United Arab Emirates, Jordan', 1], ['Sweden, Czech Republic, United Kingdom, Denmark, Netherlands', 1], [nan, 0]], 'show_graph': True, 'show_chart_controls': True}

console.log
{
  "graph_data":

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
