<template>
  <div>
    <section v-if="chartControls" class="chart_controls graph-filter-area">
      <ChartTitle />
      <div>
        <!-- change graph color div -->
        <GraphColor />
        <div class="alignment-fix">
          <div>
            <label for="two"># of columns for X-Axis:</label>
            <div class="tooltip">
              <span class="tooltiptext">Tooltip text</span>
            </div>
            <input type="number" id="title" v-model="xAxisCountNumber" />
          </div>
          <button
            type="submit"
            v-on:click="changeXAxisColumnNumber()"
            class="btn btn-outline-primary button-fix"
            v-tooltip.top="msg"
          >
            Submit
          </button>
        </div>
        <div>
          <label for="two"># of columns for Y-Axis:</label>
          <div class="tooltip">
            <span class="tooltiptext">Tooltip text</span>
          </div>
          <input type="number" id="title" v-model="yAxisCountNumber" />
          <button
            type="submit"
            v-on:click="changeYAxisColumnNumber()"
            class="btn btn-outline-primary button-fix"
            v-tooltip.top="yAxisColumnNumberMSG"
          >
            Submit
          </button>
        </div>
      </div>
      <div>
        <div class="h-axis-fix">
          <label for="two">H-Axis Label:</label>
          <input type="text" id="title" v-model="hAxisName" />
          <button
            type="submit"
            v-on:click="changeHAxisTitle()"
            class="btn btn-outline-primary button-fix"
          >
            Submit
          </button>
        </div>
        <div>
          <label for="two">V-Axis Label:</label>
          <input type="text" id="title" v-model="vAxisName" />
          <button
            type="submit"
            v-on:click="changeVAxisTitle()"
            class="btn btn-outline-primary button-fix"
          >
            Submit
          </button>
        </div>
      </div>
    </section>
    <!-- End change graph color div -->
  </div>
</template>

<script>
import ChartTitle from "@/components/data/datacomponents/filtercomponents/filterparts/MakeChartTitle.vue";
import GraphColor from "@/components/data/datacomponents/filtercomponents/filterparts/GraphColor.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "GraphFilter",
  components: {
    ChartTitle,
    GraphColor,
  },
  data() {
    return {
      xAxisCountNumber: 5,
      yAxisCountNumber: 4,
      hAxisName: "",
      vAxisName: "",
      title: "",
      // color: "blue",
      // colors: ["blue", "red", "black", "orange"],
      aggregateValueChecked: false,
      chartControls: false,
      // Need to fix this message...as well as do this better.
      msg:
        "Here you can select" +
        "</br>" +
        "how many columns you" +
        "</br>" +
        "want on the x-axis.",
      yAxisColumnNumberMSG:
        "Here you can select" +
        "</br>" +
        "how many columns you" +
        "</br>" +
        "want on the y-axis" +
        "</br>" +
        "when aggregate is selected.",
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", [
      "showGraph", // May not need this
      "showChartControls",
      "hideControlsBasedOnAggregateValueSelected",
    ]),
  },
  methods: {
    ...mapActions("data", [
      "changeGraphType",
      "changeUniqueValue",
      "changeChartTitle",
      // "changeChartColorAction",
      "changeAggregateValue",
      "changeGraphData",
      "fetchGraph",
      "changeHAxisName",
      "changeVAxisName",
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
    // makeChartTitle() {
    //   this.changeChartTitle(this.title);
    // },
    // changeChartColor() {
    //   this.changeChartColorAction(this.color);
    // },
    setShowChartControls() {
      this.chartControls = this.showChartControls;
    },
    changeXAxisColumnNumber() {
      const payload = {
        xAxisCountNumber: this.xAxisCountNumber,
        fromButton: true,
      };
      this.changeGraphData(payload);
    },
    changeYAxisColumnNumber() {
      if (this.$store.getters["data/xAxisValue"] == "") {
        alert("Please put a column in for the x-value");
      } else if (this.$store.getters["data/yAxisValue"] == "") {
        alert("Please put a column in for the y-value");
      } else {
        const payload = {
          fileName: this.$store.getters["data/fileName"],
          xAxisValue: this.$store.getters["data/xAxisValue"],
          yAxisValue: this.$store.getters["data/yAxisValue"],
          yAxisValue: this.$store.getters["data/yAxisValue"],
          uniqueValue: this.$store.getters["data/uniqueValue"],
          aggregateValue: this.$store.getters["data/aggregateValue"],
          yAxisCountNumber: this.yAxisCountNumber,
        };
        this.fetchGraph({ payload });
      }
    },
    changeHAxisTitle() {
      this.changeHAxisName(this.hAxisName);
    },
    changeVAxisTitle() {
      this.changeVAxisName(this.vAxisName);
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

.h-axis-fix {
  margin-bottom: 2%;
}
</style>