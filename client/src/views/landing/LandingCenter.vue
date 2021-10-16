<template>
  <div>
    <section>
      <div class='div-area'>Ease of Use</div>
      <div>File Types</div>
      <div>Dashboards</div>
      <div>Quick Analysis</div>
    </section>
  </div>
</template>

<script>
export default {
  name: "LandingCenter",
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.div-area {
	border: 2px solid red;
}
</style>