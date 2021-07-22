<template>
  <div>
    <section>
      <div>
        <h3 class="center font-fix">No Graph</h3>
        <p class="font-fix">
          drag a column to the x-axis and y-axis areas and then press
          "Make Graph"
        </p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "NoGraph",
};
</script>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 500px;
}

.font-fix {
  text-transform: uppercase;
}
</style>