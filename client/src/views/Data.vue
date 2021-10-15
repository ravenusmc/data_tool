<template>
  <div>
    <FileArea />
    <section v-if="showDataArea">
      <DataArea />
    </section>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import FileArea from "@/components/data/FileArea.vue";
import DataArea from "@/components/data/DataArea.vue";

export default {
  name: "TextAnalysis",
  components: {
    FileArea,
    DataArea,
  },
  computed: {
    ...mapGetters("data", ["showDataArea"]),
  },
};
</script>

<style scoped>
section {
  border-top: 3px solid black;
}
</style>