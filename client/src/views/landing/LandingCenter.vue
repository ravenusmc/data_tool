<template>
  <div>
    <section>
      <div class="div-area">
				    <a href="https://twitter.com/mcuddy7">
						<fa-icon :icon="['fas', 'usertie']" size="3x" />
						<i class="fa-solid fa-user-tie"></i>
            <!-- <fa-icon :icon="['fas', 'hashtag']" size="3x" /> -->
          </a>
        <h2>Ease of Use</h2>
      </div>
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