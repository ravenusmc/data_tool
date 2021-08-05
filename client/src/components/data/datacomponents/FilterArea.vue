<template>
  <div>
    <section class="filter-area">
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
        <label for="two">Pie Chart</label>
      </div>
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
      <div>
        <input
          v-on:input="makeChartTitle()"
          type="text"
          id="title"
          placeholder="Chart Title"
          v-model="title"
        />
        <label for="title"></label>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "FilterArea",
  data() {
    return {
      graphType: "",
      uniqueValue: "",
      title: "",
    };
  }, // End of Data
  methods: {
    ...mapActions("data", [
      "changeGraphType",
      "changeUniqueValue",
      "changeChartTitle",
    ]),
    graphTypeSelected() {
      const payload = {
        graphType: this.graphType,
      };
      this.changeGraphType(payload);
    },
    uniqueValueSelected() {
      this.changeUniqueValue(this.uniqueValue);
    },
    makeChartTitle() {
      this.changeChartTitle();
      console.log("hi");
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
</style>

