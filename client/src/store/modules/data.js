import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	columns: {},
	showDataArea: false,
	initialColumns: [],
	XAxisArray: [],
	YAxisArray: [],
};

const getters = {
	columns: state => state.columns,
	showDataArea: state => state.showDataArea,
	XAxisArray: state => state.XAxisArray,
	initialColumns: state => state.initialColumns,
	YAxisArray: state => state.YAxisArray,
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

};

const mutations = {

	setColumns(state, data) {
		state.columns = data
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

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};