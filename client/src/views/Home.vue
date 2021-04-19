<template>
  <div>
    <Navbar />
      <section>
        <img src="../assets/images/data_pic.jpg" alt="image of a graphs on a computer">
      </section>
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

<style scoped>
img {
  border: 2px solid red;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
	width: 100%;
	height: 900px;
}
</style>
