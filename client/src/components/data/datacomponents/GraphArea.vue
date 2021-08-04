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
      typeOne: "",
      chartOptionsOne: {
        title: "",
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
      "graphType",
    ]),
  },
  methods: {
    setXAxisOnGraph() {
      this.chartOptionsOne.hAxis.title = this.xAxisValue;
    },
    setYAxisOnGraph() {
      this.chartOptionsOne.vAxis.title = this.yAxisValue;
    },
    changeGraphType() {
      this.typeOne = this.graphType.graphType;
    },
  },
  watch: {
    xAxisValue: {
      handler(value) {
        if (value) {
          this.setXAxisOnGraph();
        }
      },
      immediate: true,
    },
    yAxisValue: {
      handler(value) {
        if (value) {
          this.setYAxisOnGraph();
        }
      },
      immediate: true,
    },
    graphType: {
      handler(value) {
        if (value) {
          this.changeGraphType();
        }
      },
      immediate: true,
    },
  }, // End of Watch
  mounted() {
    this.typeOne = this.$store.getters["data/graphType"];
  },
};
</script>

<style scoped>
</style>