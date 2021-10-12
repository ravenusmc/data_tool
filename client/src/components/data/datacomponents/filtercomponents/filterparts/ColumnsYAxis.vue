<template>
  <div>
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
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ColumnsYAxis",
  data() {
    return {
      yAxisCountNumber: 4,
      // Need to fix this message...as well as do this better.
      yAxisColumnNumberMSG:
        "Here you can select" +
        "</br>" +
        "how many columns you" +
        "</br>" +
        "want on the y-axis" +
        "</br>" +
        "when aggregate is selected.",
    };
  },
  methods: {
    ...mapActions("data", ["fetchGraph"]),
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
  },
};
</script>

<style scoped>
.button-fix {
  margin-left: 3%;
}
</style>