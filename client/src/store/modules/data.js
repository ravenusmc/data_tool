import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	columns: {},
	fileName: '',
	showDataArea: false,
	initialColumns: [],
	XAxisArray: [],
	YAxisArray: [],
	xAxisValue: '',
	yAxisValue: '',
	graphData: [],
	tempGraphData: [],
	showGraph: false,
	graphType: "BarChart",
	uniqueValue: true,
	aggregateValue: false,
	chartTitle: "",
	hAxisName: "",
	vAxisName: "",
	chartColor: "",
	showChartControls: false,
	hideControlsBasedOnAggregateValueSelected: true,
	hideAvisLabels: true,
	chartOptionsOne: {
		title: "",
		hAxis: {
			title: "",
		},
		vAxis: {
			title: "",
		},
		legend: { position: "top" },
		colors: [],
		height: 650,
		animation: {
			duration: 1000,
			easing: "linear",
		},
	},
};

const getters = {
	columns: state => state.columns,
	fileName: state => state.fileName,
	showDataArea: state => state.showDataArea,
	XAxisArray: state => state.XAxisArray,
	initialColumns: state => state.initialColumns,
	YAxisArray: state => state.YAxisArray,
	xAxisValue: state => state.xAxisValue,
	yAxisValue: state => state.yAxisValue,
	graphData: state => state.graphData,
	showGraph: state => state.showGraph,
	graphType: state => state.graphType,
	uniqueValue: state => state.uniqueValue,
	chartTitle: state => state.chartTitle,
	chartColor: state => state.chartColor,
	aggregateValue: state => state.aggregateValue,
	showChartControls: state => state.showChartControls,
	hideControlsBasedOnAggregateValueSelected: state => state.hideControlsBasedOnAggregateValueSelected,
	tempGraphData: state => state.tempGraphData,
	hAxisName: state => state.hAxisName,
	vAxisName: state => state.vAxisName,
	chartOptionsOne: state => state.chartOptionsOne,
	hideAvisLabels: state => state.hideAvisLabels,
};

const actions = {

	fetchFileInformation: ({ commit }, { formData }) => {
		const path = 'http://localhost:5000/fetch_File_Information';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
			.then((res) => {
				commit('setFileName', res.data.file_name)
				commit('setColumns', res.data.column_names)
				commit('setShowDataArea', true)
			})
			.catch(error => {
				console.log(error);
			})
	},

	fetchGraph: ({ commit, getters, dispatch }, payload) => {
		const path = 'http://localhost:5000/build_data_graph';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.show_user_warning) {
					const alertMessage = `The X-axis has to many unique values. The graph is showing the first 5 columns on the x-axis. If you want to see more use the Change X Axis Column Number filter.`
					commit("setGraphData", res.data.graph_data);
					commit("setShowGraph", res.data.show_graph);
					commit("setShowChartControls", res.data.show_chart_controls);
					dispatch('changeGraphData', res.data)
					alert(alertMessage)
					if (res.data.show_aggr_warning) {
						const alertMessageAggr = 'The Y Axis has multiple values that you may want to use the aggregate check box'
						alert(alertMessageAggr)
					}
				}
				else {
					const colors = ["red", "blue", "orange", "yellow", "purple",
						"green", "#0891F5", "#641684", "#F90F24", "#2AC102"]
					if (res.data.graphType != "Pie") {
						res.data.graph_data[0].push({ role: 'style' })
						for (let i = 1; i < res.data.graph_data.length; i++) {
							let color = colors[i - 1]
							let graph_color = `color: ${color}`
							res.data.graph_data[i].push(graph_color)
						}
					}
					let data_length = res.data.graph_data.length - 1
					let chart_colors = colors.slice(0, data_length)
					getters.chartOptionsOne.colors = chart_colors
					commit("setGraphData", res.data.graph_data);
					commit("setShowGraph", res.data.show_graph);
					commit("setShowChartControls", res.data.show_chart_controls);
					dispatch('changeGraphData', res.data.graph_data)
				}
			})
			.catch(error => {
				console.log(error);
			})
	},

	changeGraphData: ({ commit, getters }, payload) => {
		let tempGraphData = getters.graphData
		if (payload.fromButton) {
			tempGraphData = tempGraphData.slice(0, payload.xAxisCountNumber);
			commit('setTempGraphData', tempGraphData)
		} else if (payload.show_user_warning === true) {
			tempGraphData = tempGraphData.slice(0, 6);
			commit('setTempGraphData', tempGraphData);
		}
		else {
			commit('setTempGraphData', tempGraphData)
		}
	},

	updateXAxis: ({ commit }, payload) => {
		commit("updateXAxis", payload);
	},

	updateYAxis: ({ commit }, payload) => {
		commit("updateYAxis", payload);
	},

	updateInitialColumns: ({ commit }, payload) => {
		commit("setInitialColumns", payload);
	},

	updateXAxisValue: ({ commit }, payload) => {
		commit("setXAxisValue", payload);
	},

	updateYAxisValue: ({ commit }, payload) => {
		commit("setYAxisValue", payload);
	},

	changeGraphType: ({ commit }, payload) => {
		commit("setGraphType", payload);
	},

	changeUniqueValue: ({ commit }, payload) => {
		commit("setUniqueValue", payload);
	},

	changeAggregateValue: ({ commit, getters }, payload) => {
		commit('setAggregateValue', payload);
		getters.hideControlsBasedOnAggregateValueSelected ? commit("setAggregateValueControls", false) : commit("setAggregateValueControls", true);
	},

	changeChartTitle: ({ commit }, payload) => {
		commit("setChartTitle", payload);
	},

	changeChartColorAction: ({ commit }, payload) => {
		console.log(payload)
		commit("setChartColor", payload);
	},

	changeHAxisName: ({ commit }, payload) => {
		commit("setHAxisName", payload)
	},

	changeVAxisName: ({ commit }, payload) => {
		commit("setVAxisName", payload)
	},

	changeAxisLabelsValues: ({ commit }, payload) => {
		let showAxisLabels = payload !== 'PieChart' ? true : false;
		commit("setHideAvisLabelsValue", showAxisLabels)
	},

};

const mutations = {

	setColumns(state, data) {
		state.columns = data
	},

	setFileName(state, data) {
		state.fileName = data
	},

	setShowDataArea(state, data) {
		state.showDataArea = data
	},

	updateXAxis: (state, payload) => {
		state.XAxisArray = payload;
	},

	updateYAxis: (state, payload) => {
		state.YAxisArray = payload;
	},

	setInitialColumns: (state, payload) => {
		state.initialColumns = payload;
	},

	setXAxisValue: (state, payload) => {
		state.xAxisValue = payload;
	},

	setYAxisValue: (state, payload) => {
		state.yAxisValue = payload;
	},

	setGraphData: (state, payload) => {
		state.graphData = payload;
	},

	setTempGraphData: (state, payload) => {
		state.tempGraphData = payload;
	},

	setShowGraph: (state, payload) => {
		state.showGraph = payload;
	},

	setGraphType: (state, payload) => {
		state.graphType = payload;
	},

	setUniqueValue: (state, payload) => {
		state.uniqueValue = payload;
	},

	setAggregateValue: (state, payload) => {
		state.aggregateValue = payload;
	},

	setChartTitle: (state, payload) => {
		state.chartTitle = payload;
	},

	setChartColor: (state, payload) => {
		state.chartColor = payload
	},

	setShowChartControls: (state, data) => {
		state.showChartControls = data
	},

	setAggregateValueControls: (state, data) => {
		state.hideControlsBasedOnAggregateValueSelected = data
	},

	setHAxisName: (state, data) => {
		state.hAxisName = data
	},

	setVAxisName: (state, data) => {
		state.vAxisName = data
	},

	setHideAvisLabelsValue: (state, data) => {
		state.hideAvisLabels = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};