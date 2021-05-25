<template>
  <div>
    <section>
			<h4><span class='make-bold'>Title: </span>{{ this.textFile.file_name }}</h4>
			<h4><span class='make-bold'>Overall Sentiment: </span>{{ this.textFile.sentiment_speech_average }}</h4>
      <div>
        <p>The Overall Sentiment of the speech is: </p>
      </div>
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

section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
  border: 2px solid red;
}
</style>