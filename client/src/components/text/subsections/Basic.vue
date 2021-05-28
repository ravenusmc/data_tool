<template>
  <div>
    <section>
      <div>
        <h4>
          <span class="make-bold">Title: </span>{{ this.textFile.file_name }}
        </h4>
        <h4>
          <span class="make-bold">Overall Sentiment: </span>
            {{ this.textFile.sentiment_speech_average }}
        </h4>
      </div>
      <div>
        <p>The rating of the sentiment:</p>
      </div>
      <Guage :percentage="percentage" />
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
      percentage: this.textFile.sentiment_speech_average,
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
}

</style>