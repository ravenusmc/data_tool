<template>
  <div>
    <FilterArea />
    <section>
      <Columns />
    </section>
  </div>
</template>

<script>
import FilterArea from "@/components/data/datacomponents/FilterArea.vue";
import Columns from "@/components/data/datacomponents/Columns.vue";

export default {
  name: "DataArea",
  components: {
    FilterArea,
    Columns,
  },
};
</script>

<style scoped>
</style>