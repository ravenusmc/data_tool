<template>
  <div>
    <FilterArea />
    <section>
      <Columns />
      <GraphArea />
    </section>
  </div>
</template>

<script>
import FilterArea from "@/components/data/datacomponents/FilterArea.vue";
import Columns from "@/components/data/datacomponents/Columns.vue";
import GraphArea from "@/components/data/datacomponents/GraphArea.vue";

export default {
  name: "DataArea",
  components: {
    FilterArea,
    Columns,
    GraphArea,
  },
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: 15% 85%;
  border: 2px solid blue;
}
</style>