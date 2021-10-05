<template>
  <div>
    <div class="initial-filter-area">
      <ChartTypes />
      <UniqueValues />
      <AggValue />
    </div>
  </div>
</template>

<script>
import ChartTypes from "@/components/data/datacomponents/filtercomponents/filterparts/ChartType.vue";
import UniqueValues from "@/components/data/datacomponents/filtercomponents/filterparts/UniqueValues.vue";
import AggValue from "@/components/data/datacomponents/filtercomponents/filterparts/AggValue.vue";

export default {
  name: "InitialFilter",
  components: {
    ChartTypes,
    UniqueValues,
    AggValue,
  },
};
</script>

<style scoped>
.initial-filter-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 250px));
}
</style>