import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	fileName: '',
	textFile: {},
	showSentimentResults: false,
	initalValue: 0,
	sentence: '',
	sentenceSentiment: 0,
	textLength: 0,
	sentiment_graph_data: [],
	word_count_graph_data: [],
};

const getters = {
	fileName: state => state.fileName,
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults,
	initalValue: state => state.initalValue,
	sentence: state => state.sentence,
	sentenceSentiment: state => state.sentenceSentiment,
	textLength: state => state.textLength,
	sentiment_graph_data: state => state.sentiment_graph_data,
	word_count_graph_data: state => state.word_count_graph_data,
};

const actions = {

	clearTextState: ({ commit }) => {
		let fileName = ''
		let textFile = {}
		let showSentimentResults = false
		let initalValue = 0
		let sentence = ''
		let sentenceSentiment = 0
		let textLength = 0
		let sentiment_graph_data = []
		let word_count_graph_data = []
		commit('setFileName', fileName)
		commit('setTextFile', textFile);
		commit('setShowSentimentResults', showSentimentResults);
		commit('setInitalValue', initalValue)
		commit('setSentence', sentence)
		commit('setSentenceSentiment', sentenceSentiment)
		commit('setTextLength', textLength)
		commit('setSentiment_graph_data', sentiment_graph_data)
		commit('setWord_count_graph_data', word_count_graph_data)
	},

	handleFileUpload: ({ commit, dispatch }, { formData }) => {
		return Promise.all([
			dispatch('clearTextState'),
		])
			.then(() => {
				const path = 'http://localhost:5000/text_file_upload';
				axios.post(path, formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				})
					.then((res) => {
						commit('setFileName', res.data.file_name)
						commit('setTextFile', res.data);
						commit('setShowSentimentResults', true);
						commit('setSentence', res.data.sentence_and_sentiment_list[0].sentence)
						commit('setSentenceSentiment', res.data.sentence_and_sentiment_list[0].sentiment)
						commit('setTextLength', res.data.sentence_and_sentiment_list.length)
						commit('setSentiment_graph_data', res.data.sentiment_graph_data)
						res.data.word_count_chart_data.sort((a, b) => b[1] - a[1]);
						commit('setWord_count_graph_data', res.data.word_count_chart_data)
					})
					.catch(error => {
						console.log(error);
					})
			})
	},

	changeSentenceAndSentiment: ({ commit, getters }, { payload }) => {
		commit('setSentence', getters.textFile.sentence_and_sentiment_list[payload.value].sentence)
		commit('setSentenceSentiment', getters.textFile.sentence_and_sentiment_list[payload.value].sentiment)
		commit('setInitalValue', payload.value)
	},

	changeWordCount: ({ commit, getters }, { payload }) => {
		payload['text_file_name'] = getters.fileName
		const path = 'http://localhost:5000/change_word_count';
		axios.post(path, payload)
			.then((res) => {
				res.data.sort((a, b) => b[1] - a[1]);
				let word_data = res.data
				if (word_data.length > 10) {
					word_data = word_data.slice(0, 14)
					alert('Please Note: There were a lot of words and this is only showing the first 14')
				}
				commit('setWord_count_graph_data', word_data)
			})
			.catch(error => {
				console.log(error);
			})
	}

};

const mutations = {

	setFileName(state, data) {
		state.fileName = data
	},

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
	},

	setWord_count_graph_data(state, data) {
		state.word_count_graph_data = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};