<template>
  <div>
    <section>
			<h4>Title: TITLE.TXT</h4>
			<h4>Overall Sentiment: 0.83</h4>
      <p>{{ this.text-file }}</p>
    </section>
  </div>
</template>

<script>
export default {
  name: "Basic",
  props: ['text-file'],
  // data(){
  //   return {
  //     textFile: text-file,
  //   }
  // }
};
</script>

<style scoped>
</style>