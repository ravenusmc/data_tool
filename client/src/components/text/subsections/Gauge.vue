<template>
  <div>
    <div class='container'></div>
		<div class='fill-container' :style="{width: widthCalculation + '%'}">
		</div>
    <span>{{ widthCalculation }}%</span>
  </div>
</template>

<script>
export default {
  name: "Guage",
	props: ["percentage"],
  computed: {
    widthCalculation() {
			let correctedValue = Math.round((0.5 * this.percentage + 0.5) * 100)
			console.log(correctedValue)
      return correctedValue
    },
  },
};
</script>

<style scoped>

.container {
  width: 400px;
  height: 100px;
  top: 0;
  overflow: hidden;
	background-color: #fd7e14;
}

.fill-container {
	z-index: 1;
	height: 100px;
	top: 0;
	background-color: #007bff;
	margin-top: -100px;
}

</style>  
