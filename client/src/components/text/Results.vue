<template>
  <div>
    <h2 class="center">The Analysis</h2>
    <p>{{this.test}}</p>
    <p>{{this.name}}</p>
    <section>
      <Basic v-bind:text-file="text-file" />
      <SentenceSentiment />
    </section>
  </div>
</template>

<script>
import Basic from "@/components/text/subsections/Basic.vue";
import SentenceSentiment from "@/components/text/subsections/SentenceSentiment.vue";

export default {
  name: "Results",
  props: ['text-file'],
  components: {
    Basic,
    SentenceSentiment,
  },
  data(){
    return {
      test: text-file,
      name: "mike",
    }
  }
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