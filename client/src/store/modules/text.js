import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	textFile: {},
	showSentimentResults: false,
	initalValue: 0,
	initialSentence: '',
	sentenceSentiment: 0,
};

const getters = {
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults,
	initalValue: state => state.initalValue,
	initialSentence: state => state.initialSentence,
	sentenceSentiment: state => state.sentenceSentiment,
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
				console.log(res.data.sentence_and_sentiment_list[0])
				commit('setTextFile', res.data);
				commit('setShowSentimentResults', true);
				commit('setInitialSentence', res.data.sentence_and_sentiment_list[0].sentence)
				commit('setSentenceSentiment', res.data.sentence_and_sentiment_list[0].sentiment)
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
	},

	setInitialSentence(state, data) {
		state.initialSentence = data
	},

	setSentenceSentiment(state, data) {
		state.sentenceSentiment = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};