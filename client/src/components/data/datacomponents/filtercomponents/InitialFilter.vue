<template>
  <div>
    <div class="initial-filter-area">
      <ChartTypes/>
      <div class="filter-fix">
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
      <div class="filter-fix">
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
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ChartTypes from "@/components/data/datacomponents/filtercomponents/filterparts/ChartType.vue";

export default {
  name: "InitialFilter",
  components: {
    ChartTypes,
  },
  data() {
    return {
      graphType: "",
      uniqueValue: "",
      aggregateValueChecked: false,
      chartControls: false,
    };
  }, // End of Data
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
.initial-filter-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 250px));
}

.filter-fix {
  margin: 10px;
}
</style>