<template>
  <div>
    <Navbar />
    <Purpose />
    <p>
      {{ this.textFile }}
    </p>
    <section v-if="showSentimentResults">
    <hr />
      <Results v-bind:text-file="textFile" />
    </section>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Purpose from "@/components/text/Purpose.vue";
import Results from "@/components/text/Results.vue";
import Footer from "@/components/generic/Footer.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "TextAnalysis",
  components: {
    Navbar,
    Purpose,
    Results,
    Footer,
  },
  computed: {
    ...mapGetters('text', [
      'showSentimentResults',
      'textFile',
    ]),
  },
};
</script>

<style scoped>
</style>