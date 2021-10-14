<template>
  <div>
    <section v-if="chartControls" class="chart_controls graph-filter-area">
      <ChartTitle />
      <div>
        <GraphColor />
        <ColumnsXAxis />
        <ColumnsYAxis />
      </div>
      <div v-if="hideAvisLabels">
        <HAxisLabel />
        <VAxisLabel />
      </div>
    </section>
  </div>
</template>

<script>
import ChartTitle from "@/components/data/datacomponents/filtercomponents/filterparts/MakeChartTitle.vue";
import GraphColor from "@/components/data/datacomponents/filtercomponents/filterparts/GraphColor.vue";
import ColumnsXAxis from "@/components/data/datacomponents/filtercomponents/filterparts/ColumnsXAxis.vue";
import ColumnsYAxis from "@/components/data/datacomponents/filtercomponents/filterparts/ColumnsYAxis.vue";
import HAxisLabel from "@/components/data/datacomponents/filtercomponents/filterparts/HAxisLabel.vue";
import VAxisLabel from "@/components/data/datacomponents/filtercomponents/filterparts/VAxisLabel.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "GraphFilter",
  components: {
    ChartTitle,
    GraphColor,
    ColumnsXAxis,
    ColumnsYAxis,
    HAxisLabel,
    VAxisLabel,
  },
  data() {
    return {
      xAxisCountNumber: 5,
      title: "",
      aggregateValueChecked: false,
      chartControls: false,
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", [
      "showGraph", // May not need this
      "showChartControls",
      "hideControlsBasedOnAggregateValueSelected",
      "hideAvisLabels",
    ]),
  },
  methods: {
    ...mapActions("data", [
      "changeGraphType",
      "changeUniqueValue",
      "changeChartTitle",
      "changeAggregateValue",
    ]),
    graphTypeSelected() {
      // This needs to be fixed...don't need payload here
      const payload = {
        graphType: this.graphType,
      };
      this.changeGraphType(payload);
    },
    uniqueValueSelected() {
      this.changeUniqueValue(this.uniqueValue);
    },
    aggregateValueSelected() {
      this.changeAggregateValue(this.aggregateValueChecked);
    },
    setShowChartControls() {
      this.chartControls = this.showChartControls;
    },
  },
  watch: {
    showChartControls: {
      handler(value) {
        if (value) {
          this.setShowChartControls();
        }
      },
      immediate: true,
    },
  },
};
</script>

<style scoped>
.graph-filter-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 450px));
  height: 350px;
}

.align {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 10px;
}

.button-fix {
  margin-left: 3%;
}
</style>