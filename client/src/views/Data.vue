<template>
  <div>
    <Navbar />
    <h1>Data</h1>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  name: "TextAnalysis",
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style scoped>
</style>