import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	textFile: {},
	showSentimentResults: false,
	initalValue: 0,
};

const getters = {
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults,
	initalValue: state => state.initalValue,
};

const actions = {

	handleFileUpload: ({ commit }, { formData }) => {
		// console.log(payload)
		const path = 'http://localhost:5000/text_file_upload';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
			.then((res) => {
				// console.log(res.data)
				commit('setTextFile', res.data);
				commit('setShowSentimentResults', true);
			})
			.catch(error => {
				console.log(error);
			})
	},

};

const mutations = {

	setTextFile(state, data) {
		state.textFile = data
	},

	setShowSentimentResults(state, data) {
		state.showSentimentResults = data
	},

	setInitalValue(state, data) {
		state.initalValue = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};