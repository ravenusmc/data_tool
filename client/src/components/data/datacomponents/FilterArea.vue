<template>
  <div>
    <section>
      <div>
        <input type="radio" id="one" value="BarChart" v-model="graphType" />
        <label for="one">Bar Chart</label>
        <br />
        <input
          @change="test()"
          type="radio"
          id="two"
          value="PieChart"
          v-model="graphType"
        />
        <label for="two">Pie Chart</label>
        <br />
        <span>Picked: {{ graphType }}</span>
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
    test() {
      console.log("hi");
    },
  },
};
</script>

<style scoped>
.x-axis {
  border: 2px solid red;
  height: 80px;
}
</style>

