<template>
  <div>
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
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "AggValue",
  data() {
    return {
      aggregateValueChecked: false,
      chartControls: false,
    };
  }, // End of Data
  methods: {
    ...mapActions("data", ["changeAggregateValue"]),
    aggregateValueSelected() {
      this.changeAggregateValue(this.aggregateValueChecked);
    },
  },
};
</script>

<style scoped>
.filter-fix {
  margin: 10px;
}
</style>