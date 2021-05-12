<template>
  <div>
    <Navbar />
    <Purpose />
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Purpose from "@/components/text/Purpose.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  name: "TextAnalysis",
  components: {
    Navbar,
    Purpose,
    Footer,
  },
};
</script>

<style scoped>
</style>