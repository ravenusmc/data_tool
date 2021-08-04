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
	showGraph: false,
	graphType: "BarChart",
	uniqueValue: true,
	chartTitle: "",
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

	fetchGraph: ({ commit }, payload) => {
		const path = 'http://localhost:5000/build_data_graph';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.show_user_warning) {
					alert('You X-axis has to many unique values. Please try selecting a different X-Axis Value')
				} else {
					res.data.graph_data.sort((a, b) => b[1] - a[1]);
					commit("setGraphData", res.data.graph_data);
					commit("setShowGraph", res.data.show_graph);
				}
			})
			.catch(error => {
				console.log(error);
			})
	},

	changeGraphType: ({ commit }, payload) => {
		commit("setGraphType", payload);
	},

	changeUniqueValue: ({ commit }, payload) => {
		commit("setUniqueValue", payload);
	}

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

	setShowGraph: (state, payload) => {
		state.showGraph = payload;
	},

	setGraphType: (state, payload) => {
		state.graphType = payload;
	},

	setUniqueValue: (state, payload) => {
		state.uniqueValue = payload;
	},

	setChartTitle: (state, payload) => {
		state.chartTitle = payload;
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};