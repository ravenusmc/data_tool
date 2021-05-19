<template>
  <div>
    <h2 class="center">The Analysis</h2>
    <section>
      <Basic v-bind:text-file="textFile" />
      <SentenceSentiment />
    </section>
  </div>
</template>

<script>
import Basic from "@/components/text/subsections/Basic.vue";
import SentenceSentiment from "@/components/text/subsections/SentenceSentiment.vue";
import { mapGetters } from "vuex";

export default {
  name: "Results",
  components: {
    Basic,
    SentenceSentiment,
  },
  computed: {
    ...mapGetters("text", ["textFile"]),
  },
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  grid-gap: 3em;
  justify-items: center;
}
</style>