<template>
  <div>
    <section>
      <h4>
        <span class="make-bold">Title: </span>{{ this.textFile.file_name }}
      </h4>
      <h4>
        <span class="make-bold">Overall Sentiment: </span>
        <p class="sentiment-color">
          {{ this.textFile.sentiment_speech_average }}
        </p>
      </h4>
      <div>
        <p>The Overall Sentiment of the speech is:</p>
      </div>
      <Guage percentage="33" />
    </section>
  </div>
</template>

<script>
import Guage from "@/components/text/subsections/Gauge.vue";

export default {
  name: "Basic",
  components: {
    Guage,
  },
  props: {
    textFile: Object,
  },
  data() {
    return {
      sentimentClass: '',
    };
  },
};
</script>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
  /* border: 2px solid red; */
}
</style>