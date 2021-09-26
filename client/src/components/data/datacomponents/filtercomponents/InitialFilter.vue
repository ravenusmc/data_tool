<template>
  <div>
    <div class="filter-area">
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
      <div v-if="hideControlsBasedOnAggregateValueSelected">
        <input
          @change="graphTypeSelected()"
          type="radio"
          id="two"
          value="PieChart"
          v-model="graphType"
        />
        <label for="two">Pie Chart</label>
      </div>
      <br />
      <input
        @change="graphTypeSelected()"
        type="radio"
        id="two"
        value="ColumnChart"
        v-model="graphType"
      />

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
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "InitialFilter",
  data() {
    return {
      graphType: "",
      uniqueValue: "",
      aggregateValueChecked: false,
      chartControls: false,
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", ["hideControlsBasedOnAggregateValueSelected"]),
  },
  methods: {
    ...mapActions("data", [
      "changeGraphType",
      "changeUniqueValue",
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
  },
};
</script>

<style scoped>
.filter-area {
  border: 2px solid red;
  border-bottom: 2px solid black;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 250px;
}
</style>