<template>
  <div>
    <div class="align">
      <input type="text" id="title" placeholder="Chart Title" v-model="title" />
      <button
        type="submit"
        v-on:click="makeChartTitle()"
        class="btn btn-outline-primary button-fix"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ChartTitle",
  methods: {
    ...mapActions("data", ["changeChartTitle"]),
    makeChartTitle() {
      this.changeChartTitle(this.title);
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