<template>
  <div>
    <Navbar />
    <Purpose />
    <section v-if="showSentimentResults">
    <hr />
    </section>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Purpose from "@/components/text/Purpose.vue";
import Footer from "@/components/generic/Footer.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "TextAnalysis",
  components: {
    Navbar,
    Purpose,
    Footer,
  },
  computed: {
    ...mapGetters('text', [
			'showSentimentResults',
    ]),
  },
};
</script>

<style scoped>
</style>