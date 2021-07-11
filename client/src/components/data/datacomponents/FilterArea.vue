<template>
  <div>
    <div>
      <div :id="id" @dragover.prevent @drop.prevent="drop">X-Axis:</div>
      <div>Y-Axis:</div>
    </div>
    <button type="submit" class="btn btn-outline-primary">Make Graph</button>
  </div>
</template>

<script>
export default {
  name: "FilterArea",
  props: ["id"],
  methods: {
    drop: (e) => {
      const card_id = e.dataTransfer.getData("card_id");
      const card = document.getElementById(card_id);
      card.style.display = "block";
      e.target.appendChild(card);
    },
  },
};
</script>

<style scoped>
</style>

