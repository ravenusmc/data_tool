<template>
  <div>
    <Purpose />
    <section v-if="showSentimentResults">
      <hr />
      <Results />
    </section>
  </div>
</template>

<script>
import Purpose from "@/components/text/Purpose.vue";
import Results from "@/components/text/Results.vue";
import { mapGetters } from "vuex";

export default {
  name: "TextAnalysis",
  components: {
    Purpose,
    Results,
  },
  computed: {
    ...mapGetters("text", ["showSentimentResults"]),
  },
};
</script>

<style scoped>
section {
  margin: 100px 50px 100px 50px;
}
</style>