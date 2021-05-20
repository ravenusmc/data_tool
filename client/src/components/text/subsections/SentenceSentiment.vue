<template>
  <div>
    <section>
			<h4>Sentence: {{ this.textFile.first_sentence }}</h4>
			<br>
			<h4>Sentence Sentiment: {{ this.textFile.first_sentence_sentiment }}</h4>
			<h4>Change Sentence:</h4>
			<div>
				<svg
				@click="changeSentence('up')"
				width="3em"
				height="3em"
				viewBox="0 0 16 16"
				class="bi bi-arrow-up-circle-fill svgLeft"
				fill="currentColor" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd"
					d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354
					7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5
					5.707V11.5z"/>
				</svg>
				<svg @click="changeSentence('down')" width="3em" height="3em" viewBox="0 0 16 16"
					class="bi bi-arrow-down-circle-fill svgRight"
					fill="currentColor" xmlns="http://www.w3.org/2000/svg">
					<path fill-rule="evenodd" d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5
					4.5a.5.5 0 0 0-1
					0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0
					0-.708-.708L8.5 10.293V4.5z"/>
				</svg>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "SentenceSentiment",
  props: {
    textFile: Object,
  },
	// data() {
  //   return {
  //     value: this.initalValue,
  //   };
  // },
	methods: {
    // ...mapActions([
    //   'fireActions',
    //   'fetchSpeechSentenceSentiment',
    // ]),
    changeSentence(direction) {
			console.log(direction)
			// let value = this.initalValue;
			// console.log(value)
      // if (direction === 'up') {
      //   value += 1;
      // } else if (direction === 'down') {
      //   value -= 1;
      // }
      // if (value > this.speechLength) {
      //   alert('The end of the speech has been reached!');
      // } else if (value < 0) {
      //   alert('You cannot go back any further');
      // } else {
        // const payload = {
        //   value,
        //   speech: this.selectedSpeech,
        // };
        // this.fetchSpeechSentenceSentiment({ payload });
      // }
    },
  },
};
</script>

<style scoped>
</style>