<template>
  <div>
    <section>
      <div v-if="!showGraph">
        <NoGraph />
      </div>
      <div v-if="showGraph">
        <GraphCard
          :typeOne="typeOne"
          :data="graphData"
          :options="chartOptionsOne"
        >
        </GraphCard>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GraphCard from "@/components/charts/GraphCard.vue";
import NoGraph from "@/components/data/datacomponents/NoGraph.vue";

export default {
  name: "GraphArea",
  components: {
    GraphCard,
    NoGraph,
  },
  data() {
    return {
      typeOne: "BarChart",
      chartOptionsOne: {
        title: "Chart",
        hAxis: {
          title: "",
        },
        vAxis: {
          title: "",
        },
        legend: { position: "top" },
        colors: ["#007bff"],
        height: 650,
        animation: {
          duration: 1000,
          easing: "linear",
        },
      },
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", [
      "graphData",
      "xAxisValue",
      "yAxisValue",
      "showGraph",
    ]),
  },
  created() {
    //this.chartOptionsOne.hAxis.title = this.$store.getters["data/xAxisValue"];
    this.chartOptionsOne.vAxis.title = this.$store.getters["data/yAxisValue"];
  },
};
</script>

<style scoped>
</style>