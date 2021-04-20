<template>
  <div>
    <Navbar />
      <section>
        <div class='title-div'>
          <h1 class='title_header'>Data Tool</h1>
        </div>
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

section {
  background-image: url('../assets/images/data_pic.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
	/* width: 100%; */
	height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title_header {
  font-size: 9rem;
  font-weight: 600;
  letter-spacing: -.3rem;
  color: #fff;
}

.title-div {
  background-color: rgba(255, 0, 0, 0.8);
}

</style>
