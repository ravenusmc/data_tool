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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 500px));
  justify-content: center;
}
</style>

