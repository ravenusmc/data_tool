<template>
  <div>
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
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "UniqueValues",
  data() {
    return {
      uniqueValue: "",
    };
  }, // End of Data
  methods: {
    ...mapActions("data", ["changeUniqueValue"]),
    uniqueValueSelected() {
      this.changeUniqueValue(this.uniqueValue);
    },
  },
};
</script>

<style scoped>
.filter-fix {
  margin: 10px;
}
</style>