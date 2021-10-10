<template>
  <div>
    <div class="align">
      <label class="font">Color:</label>&nbsp;
      <select v-model="color" name="colot">
        <option v-for="color in colors" v-bind:key="color" :value="color">
          {{ color }}
        </option>
      </select>
      <button
        type="submit"
        v-on:click="changeChartColor()"
        class="btn btn-outline-primary button-fix"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ChartColor",
  data() {
    return {
      color: "blue",
      colors: ["blue", "red", "black", "orange"],
    };
  }, // End of Data
  methods: {
    ...mapActions("data", ["changeChartColorAction"]),
    changeChartColor() {
      this.changeChartColorAction(this.color);
    },
  },
};
</script>

<style scoped>
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
