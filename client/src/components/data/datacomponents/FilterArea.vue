<template>
  <div>
    <section class="filter-area">
      <div>
        <h3>Pick Chart Type:</h3>
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
    </section>
  </div>
</template>

<script>
export default {
  name: "FilterArea",
  data() {
    return {
      graphType: "",
    };
  }, // End of Data
  methods: {
    //...mapActions("text", ["changeSentenceAndSentiment"]),
    graphTypeSelected() {
      const payload = {
        graphType: this.graphType,
      };
      console.log(payload);
      // this.changeSentenceAndSentiment({ payload });
    },
  },
};
</script>

<style scoped>
.filter-area {
  border-bottom: 2px solid black;
}

.x-axis {
  border: 2px solid red;
  height: 80px;
}
</style>

