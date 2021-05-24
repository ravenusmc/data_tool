<template>
  <div>
    <Navbar />
    <Purpose />
    <section v-if="showSentimentResults">
      <hr />
      <Results />
    </section>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Purpose from "@/components/text/Purpose.vue";
import Results from "@/components/text/Results.vue";
import Footer from "@/components/generic/Footer.vue";
import { mapGetters } from "vuex";

export default {
  name: "TextAnalysis",
  components: {
    Navbar,
    Purpose,
    Results,
    Footer,
  },
  computed: {
    ...mapGetters("text", ["showSentimentResults"]),
  },
};
</script>

<style scoped>
section {
  margin-top: 100px;
  margin-bottom: 100px;
}
</style>