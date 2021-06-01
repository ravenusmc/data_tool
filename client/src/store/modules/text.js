import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	textFile: {},
	showSentimentResults: false,
	initalValue: 0,
	sentence: '',
	sentenceSentiment: 0,
	textLength: 0,
	sentiment_graph_data: [],
};

const getters = {
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults,
	initalValue: state => state.initalValue,
	sentence: state => state.sentence,
	sentenceSentiment: state => state.sentenceSentiment,
	textLength: state => state.textLength,
	sentiment_graph_data: state => state.sentiment_graph_data,
};

const actions = {

	handleFileUpload: ({ commit }, { formData }) => {
		const path = 'http://localhost:5000/text_file_upload';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
			.then((res) => {
				console.log(res.data)
				commit('setTextFile', res.data);
				commit('setShowSentimentResults', true);
				commit('setSentence', res.data.sentence_and_sentiment_list[0].sentence)
				commit('setSentenceSentiment', res.data.sentence_and_sentiment_list[0].sentiment)
				commit('setTextLength', res.data.sentence_and_sentiment_list.length)
				commit('setSentiment_graph_data', res.data.sentiment_graph_data)
			})
			.catch(error => {
				console.log(error);
			})
	},

	changeSentenceAndSentiment: ({ commit, getters }, { payload }) => {
		commit('setSentence', getters.textFile.sentence_and_sentiment_list[payload.value].sentence)
		commit('setSentenceSentiment', getters.textFile.sentence_and_sentiment_list[payload.value].sentiment)
		commit('setInitalValue', payload.value)
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

	setSentence(state, data) {
		state.sentence = data
	},

	setSentenceSentiment(state, data) {
		state.sentenceSentiment = data
	},

	setTextLength(state, data) {
		state.textLength = data
	},

	setSentiment_graph_data(state, data) {
		state.sentiment_graph_data = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};