<template>
  <div>
    <section class="filter-area">
      <InitialFilter />
      <GraphFilter />
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import InitialFilter from "@/components/data/datacomponents/filtercomponents/InitialFilter.vue";
import GraphFilter from "@/components/data/datacomponents/filtercomponents/GraphFilter.vue";

export default {
  name: "FilterArea",
  components: {
    InitialFilter,
    GraphFilter,
  },
};
</script>

<style scoped>
.filter-area {
  border-bottom: 2px solid black;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 250px;
}

.x-axis {
  border: 2px solid red;
  height: 80px;
}

.chart_controls {
  border: 2px solid red;
}
</style>

