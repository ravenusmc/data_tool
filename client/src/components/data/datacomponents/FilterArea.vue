<template>
  <div>
    <section class="filter-area">
      <!-- Chart type div -->
      <div>
        <h6>Pick Chart Type:</h6>
        <input
          @change="graphTypeSelected()"
          type="radio"
          id="one"
          value="BarChart"
          v-model="graphType"
        />
        <label for="one">Bar Chart</label>
        <br />
        <input
          @change="graphTypeSelected()"
          type="radio"
          id="two"
          value="PieChart"
          v-model="graphType"
        />
        <div v-if="hideControlsBasedOnAggregateValueSelected">
          <label for="two">Pie Chart</label>
          <br />
          <input
            @change="graphTypeSelected()"
            type="radio"
            id="two"
            value="ColumnChart"
            v-model="graphType"
          />
        </div>
        <label for="two">Column Chart</label>
      </div>
      <!-- End chart type div -->
      <!-- unique values div -->
      <div>
        <h6>Unique Values: (Y - Axis)</h6>
        <input
          @change="uniqueValueSelected()"
          type="radio"
          id="one"
          value="true"
          v-model="uniqueValue"
        />
        <label for="one">Unique Values - Y Axis</label>
        <br />
        <input
          @change="uniqueValueSelected()"
          type="radio"
          id="two"
          value="False"
          v-model="uniqueValue"
        />
        <label for="two">All Values - Y Axis</label>
      </div>
      <!-- End unique values div -->
      <!-- Aggregate div -->
      <div>
        <h6>Use Aggregate Value</h6>
        <input
          @change="aggregateValueSelected()"
          type="checkbox"
          id="checkbox"
          value="true"
          v-model="aggregateValueChecked"
        />
        <label for="checkbox">Aggregate Value Y Axis</label>
      </div>
      <!-- End Aggregate div -->
      <section v-if="chartControls" class="chart_controls">
        <!-- change graph Title div -->
        <div>
          <input
            type="text"
            id="title"
            placeholder="Chart Title"
            v-model="title"
          />
          <button
            type="submit"
            v-on:click="makeChartTitle()"
            class="btn btn-outline-primary"
          >
            Change Chart Title
          </button>
        </div>
        <!-- End change graph Title div -->
        <!-- change graph color div -->
        <div>
          <label class="font">Color:</label>&nbsp;
          <select v-model="color" name="colot">
            <option v-for="color in colors" v-bind:key="color" :value="color">
              {{ color }}
            </option>
          </select>
          <button
            type="submit"
            v-on:click="changeChartColor()"
            class="btn btn-outline-primary"
          >
            Change Chart Color
          </button>
        </div>
        <div>
          <label for="two"># of columns for X-Axis:</label>
          <div class="tooltip">
            <span class="tooltiptext">Tooltip text</span>
          </div>
          <input type="number" id="title" v-model="xAxisCountNumber" />
          <button
            type="submit"
            v-on:click="changeXAxisColumnNumber()"
            class="btn btn-outline-primary"
            v-tooltip.top="msg"
          >
            Change X Axis Column Number
          </button>
        </div>
      </section>
      <!-- End change graph color div -->
    </section>
  </div>
</template>
Logistics Officer, 2009-2014, Central Intelligence Agency (CIA)
<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "FilterArea",
  data() {
    return {
      graphType: "",
      uniqueValue: "",
      xAxisCountNumber: 5,
      title: "",
      color: "blue",
      colors: ["blue", "red", "black", "orange"],
      aggregateValueChecked: false,
      chartControls: false,
      msg: "This is a button.  " + '</br>' + "This is a button.  ",
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", [
      "showGraph",
      "showChartControls",
      "hideControlsBasedOnAggregateValueSelected",
    ]),
  },
  methods: {
    ...mapActions("data", [
      "changeGraphType",
      "changeUniqueValue",
      "changeChartTitle",
      "changeChartColorAction",
      "changeAggregateValue",
      "changeGraphData",
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
    makeChartTitle() {
      this.changeChartTitle(this.title);
    },
    changeChartColor() {
      this.changeChartColorAction(this.color);
    },
    setShowChartControls() {
      this.chartControls = this.showChartControls;
    },
    changeXAxisColumnNumber() {
      this.changeGraphData(this.xAxisCountNumber);
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
.filter-area {
  border-bottom: 2px solid black;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.x-axis {
  border: 2px solid red;
  height: 80px;
}

.chart_controls {
  border: 2px solid red;
}

</style>

