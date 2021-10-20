<template>
  <div>
    <section>
      <div class="title-div" :style="{ filter: blurCalculation }">
        <h1 class="title_header center">Data Tool</h1>
        <h4 class="sub_title_header">A Simple Data Tool for the Masses</h4>
      </div>
    </section>
    <LandingCenter />
    <DataToolBackGround />
  </div>
</template>

<script>
import LandingCenter from "@/views/landing/LandingCenter.vue";
import DataToolBackGround from "@/views/landing/DataToolBackGround.vue";

export default {
  name: "Home",
  components: {
    LandingCenter,
    DataToolBackGround,
  },
  computed: {
    blurCalculation() {
      return "blur(1.2px)";
    },
  },
};
</script>

<style scoped>
section {
  background-image: url("../assets/images/landing_2.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 70vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title-div {
  background: rgba(0, 0, 0, 0.7);
  padding: 20px;
}

.title_header {
  font-size: 6rem;
  font-weight: 600;
  letter-spacing: -0.3rem;
  text-transform: uppercase;
  color: white;
}

.sub_title_header {
  font-size: 2rem;
  font-weight: 300;
  letter-spacing: 0.3rem;
  text-transform: uppercase;
  color: white;
}
</style>
