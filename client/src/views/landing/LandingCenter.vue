<template>
  <div>
    <section>
      <div class="div-area">
        <div class="icon-area">
          <i class="ri-drag-move-2-fill ri-4x"></i>
        </div>
        <div class="paragraph-div">
          <h2>Ease of Use</h2>
          <p>
            Data Tool is a simple, easy to use tool that allows the user to do
            some basic data analysis.
          </p>
        </div>
      </div>
      <div class="div-area">
        <i class="ri-file-line ri-4x"></i>
        <h2>File Types</h2>
      </div>
      <div class="div-area">
        <i class="ri-dashboard-2-fill ri-4x"></i>
        <h2>Dashboards</h2>
      </div>
      <div class="div-area">
        <i class="ri-speed-fill ri-4x"></i>
        <h2>Quick Analysis</h2>
      </div>
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
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  /* border: 2px solid black; */
  margin: 60px;
}

.paragraph-div {
  border-left: 1px solid #dedede;
  padding-left: 30px;
}

.icon-area {
  padding-right: 15px;
}

</style>