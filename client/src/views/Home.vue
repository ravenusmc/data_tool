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
  margin: 25px;
  background-image: url('../assets/images/data_pic.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
	height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title_header {
  font-size: 6rem;
  font-weight: 600;
  letter-spacing: -.3rem;
  color: rgb(225, 100, 0);
}

.title-div {
  background-color: rgba(0, 125, 225, 0.8);
  padding: 20px;
}

</style>
