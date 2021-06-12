<template>
  <div>
    <h2 class="center">The Analysis</h2>
    <section>
      <Basic v-bind:text-file="textFile" />
      <SentenceSentiment v-bind:text-file="textFile" />
    </section>
    <hr>
    <SentimentGraph />
    <hr>
    <WordCountGraph />
    <div class="word-count-area">
      <WordCountFilter />
      <WordCountExplanation />
    </div>
  </div>
</template>

<script>
import Basic from "@/components/text/subsections/Basic.vue";
import SentenceSentiment from "@/components/text/subsections/SentenceSentiment.vue";
import SentimentGraph from "@/components/text/subsections/SentimentGraph.vue";
import WordCountGraph from "@/components/text/subsections/WordCountGraph.vue";
import WordCountFilter from "@/components/text/subsections/WordCountFilter.vue";
import WordCountExplanation from "@/components/text/subsections/WordCountExplanation.vue";
import { mapGetters } from "vuex";

export default {
  name: "Results",
  components: {
    Basic,
    SentenceSentiment,
    SentimentGraph,
    WordCountGraph,
    WordCountFilter,
    WordCountExplanation,
  },
  computed: {
    ...mapGetters("text", ["textFile"]),
  },
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 3em;
  justify-items: center;
}

.word-count-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 3em;
  justify-items: center;
  margin-top: 50px;
}
</style>