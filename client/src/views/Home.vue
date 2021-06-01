<template>
  <div>
    <section>
      <div class="title-div" :style="{ filter: blurCalculation }">
        <h1 class="title_header">Data Tool</h1>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Home",
  computed: {
    blurCalculation() {
      return "blur(1.2px)";
    },
  }
};
</script>

<style scoped>
section {
  background-image: url("../assets/images/landing.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title-div {
  background: hsla(240, 100%, 100%, 0.7);
  padding: 20px;
}

.title_header {
  font-size: 6rem;
  font-weight: 600;
  letter-spacing: -0.3rem;
  text-transform: uppercase;
}
</style>
