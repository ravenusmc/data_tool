<template>
  <div>
    <div class="filter-fix">
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
      <input
        @change="graphTypeSelected()"
        type="radio"
        id="two"
        value="ColumnChart"
        v-model="graphType"
      />
      <label for="two">Column Chart</label>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ChartTypes",
  data() {
    return {
      graphType: "",
    };
  }, // End of Data
  computed: {
    ...mapGetters("data", ["hideControlsBasedOnAggregateValueSelected"]),
  },
  methods: {
    ...mapActions("data", ["changeGraphType"]),
    graphTypeSelected() {
      // This needs to be fixed...don't need payload here
      const payload = {
        graphType: this.graphType,
      };
      this.changeGraphType(payload);
    },
  },
};
</script>

<style scoped>
.filter-fix {
  margin: 10px;
}
</style>