<template>
  <div>
    <div>
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
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ColumnsXAxis",
  data() {
    return {
      xAxisCountNumber: 5,
      // Need to fix this message...as well as do this better.
      msg:
        "Here you can select" +
        "</br>" +
        "how many columns you" +
        "</br>" +
        "want on the x-axis.",
    };
  },
  methods: {
    ...mapActions("data", ["changeGraphData"]),
    changeXAxisColumnNumber() {
      const payload = {
        xAxisCountNumber: this.xAxisCountNumber,
        fromButton: true,
      };
      this.changeGraphData(payload);
    },
  },
};
</script>

<style scoped>
.button-fix {
  margin-left: 3%;
}
</style>