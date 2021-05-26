<template>
  <div>
    <div></div>
    <span>{{ percentage }}%</span>
  </div>
</template>

<script>
export default {
  name: "Guage",
  props: ["percentage"],
  computed: {
    rotate() {
      const v = (this.percentage * 180) / 100;
      return `rotate(${v}deg)`;
    },
  },
};
</script>

<style scoped>
/* body { 
  background-color: #4d4d4d; 
} */

/* @gauge-width: 400px;
@gauge-heigth: @gauge-width / 2;
@gauge-bar-width: 75px;
@middle-width: @gauge-width - (@gauge-bar-width * 2);

@gauge-color: #5df086;
@gauge-bg-color: lighten(@gauge-color, 15%); */

.container {
  width: 400px;
  height: 200px;
  top: 0;
  overflow: hidden;
  border: 2px solid red;
}

.gauge-bg {
  z-index: 1;
  width: 200px;
  height: 200px;
  background-color: red;
  /* background-color: lighten("#5df086", 15%); */
  border-radius: 250 250 0 0;
  border: 2px solid blue;
}

.gauge-middle {
  z-index: 3;
  /* position: absolute; */
  background-color: #4d4d4d;
  width: 400px;
  height: calc(250px);
  top: 75px;
  margin-left: 75px;
  margin-right: auto;
  border-radius: 250px 250px 0 0;
  border: 2px solid yellow;
}

.gauge-overlay {
  z-index: 2;
  /* position: absolute; */
  background-color: #5df086;
  width: 400px;
  height: 200px;
  top: 200px;
  border-radius: 0 0 200px 200px;
  transform-origin: center top;
}

.gauge-data {
  z-index: 4;
  color: #5df086;
  /* position: absolute; */
  width: 400px;
  bottom: 0;
  text-align: center;
  font-size: 24px;
}
</style>  

<!-- <div class="container">
    <div class="gauge-bg"></div>
    <div class="gauge-middle"></div>
    <div class="gauge-overlay" :style="{ transform: rotate }"></div>
    <div class="gauge-data">
      <span>{{ percentage }}%</span>
    </div>
  </div> -->