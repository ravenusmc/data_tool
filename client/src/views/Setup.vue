<template>
  <div>
    <Navbar />
		Set Up
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  name: "Home",
	components: {
    Navbar,
    Footer,
  },
};
</script>