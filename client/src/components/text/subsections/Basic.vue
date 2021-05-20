<template>
  <div>
    <section>
			<h4>Title: {{ this.textFile.file_name }}</h4>
			<h4>Overall Sentiment: {{ this.textFile.sentiment_speech_average }}</h4>
    </section>
  </div>
</template>

<script>
export default {
  name: "Basic",
  props: {
    textFile: Object,
  }
};
</script>

<style scoped>
</style>