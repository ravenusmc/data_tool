<template>
  <div>
    <h2 class="center">The Analysis</h2>
    <section>
      <Basic v-bind:text-file="textFile" />
      <SentenceSentiment v-bind:text-file="textFile" />
    </section>
    <SentimentGraph />
    <WordCountGraph />
    <WordCountFilter />
  </div>
</template>

<script>
import Basic from "@/components/text/subsections/Basic.vue";
import SentenceSentiment from "@/components/text/subsections/SentenceSentiment.vue";
import SentimentGraph from "@/components/text/subsections/SentimentGraph.vue";
import WordCountGraph from "@/components/text/subsections/WordCountGraph.vue";
import WordCountFilter from "@/components/text/subsections/WordCountFilter.vue";
import { mapGetters } from "vuex";

export default {
  name: "Results",
  components: {
    Basic,
    SentenceSentiment,
    SentimentGraph,
    WordCountGraph,
    WordCountFilter,
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
</style>