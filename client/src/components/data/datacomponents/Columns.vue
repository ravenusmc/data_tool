<template>
  <div>
    <section>
      <div class="axis">
        <h6>X-Axis:</h6>
        <draggable v-model="XAxisArray" group="columnNames" @change="log">
          <div
            v-for="column in XAxisArray"
            :key="column.index"
            :id="column.index"
            class="column-name-div"
          >
            {{ column.name }}
          </div>
        </draggable>
      </div>
      <div class="axis">
        <h6>Y-Axis:</h6>
        <draggable v-model="YAxisArray" group="columnNames">
          <div
            v-for="column in YAxisArray"
            :key="column.index"
            :id="column.index"
            class="column-name-div"
          >
            {{ column.name }}
          </div>
        </draggable>
      </div>
      <div class="button-div">
        <button
          type="submit"
          v-on:click="makeGraph()"
          class="btn btn-outline-primary"
        >
          Make Graph
        </button>
      </div>
      <h3 class="center">Columns</h3>
      <draggable v-model="initialColumns" group="columnNames">
        <div
          v-for="column in initialColumns"
          :key="column.index"
          :id="column.index"
          class="column-name-div"
        >
          <p>{{ column.name }}</p>
        </div>
      </draggable>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import draggable from "vuedraggable";

export default {
  name: "Columns",
  components: {
    draggable,
  },
  computed: {
    ...mapGetters("data", [
      "columns",
      "XAxisArray",
      "initialColumns",
      "YAxisArray",
      "fileName:",
    ]),
    XAxisArray: {
      get() {
        return this.$store.state.data.XAxisArray;
      },
      set(value) {
        this.$store.dispatch("data/updateXAxis", value);
        this.$store.dispatch("data/updateXAxisValue", value[0].name);
        if (this.$store.getters["data/XAxisArray"].length > 1) {
          let poppedValue = this.$store.getters["data/XAxisArray"].pop();
          this.$store.getters["data/initialColumns"].push(poppedValue);
          this.$store.dispatch(
            "data/updateInitialColumns",
            this.$store.getters["data/initialColumns"]
          );
        }
      },
    },
    YAxisArray: {
      get() {
        return this.$store.state.data.YAxisArray;
      },
      set(value) {
        this.$store.dispatch("data/updateYAxis", value);
        this.$store.dispatch("data/updateYAxisValue", value[0].name);
        if (this.$store.getters["data/YAxisArray"].length > 1) {
          let poppedValue = this.$store.getters["data/YAxisArray"].pop();
          this.$store.getters["data/initialColumns"].push(poppedValue);
          this.$store.dispatch(
            "data/updateInitialColumns",
            this.$store.getters["data/initialColumns"]
          );
        }
      },
    },
    initialColumns: {
      get() {
        return this.$store.state.data.initialColumns;
      },
      set(value) {
        this.$store.dispatch("data/updateInitialColumns", value);
      },
    },
  },
  methods: {
    ...mapActions("data", ["fetchGraph"]),
    makeGraph() {
      if (this.$store.getters["data/xAxisValue"] == "") {
        alert("Please put a column in for the x-value");
      } else if (this.$store.getters["data/yAxisValue"] == "") {
        alert("Please put a column in for the y-value");
      } else {
        const payload = {
          fileName: this.$store.getters["data/fileName"],
          xAxisValue: this.$store.getters["data/xAxisValue"],
          yAxisValue: this.$store.getters["data/yAxisValue"],
          yAxisValue: this.$store.getters["data/yAxisValue"],
          uniqueValue: this.$store.getters["data/uniqueValue"],
          aggregateValue: this.$store.getters["data/aggregateValue"],
          yAxisCountNumber: 3,
        };
        this.fetchGraph({ payload });
      }
    },
    log: function (event) {
      console.log(event);
    },
  },
  mounted() {
    this.$store.dispatch(
      "data/updateInitialColumns",
      this.$store.getters["data/columns"]
    );
  },
};
</script>

<style scoped>
section {
  border-right: 2px solid black;
}

.axis {
  border: 2px solid black;
  height: 80px;
  margin: 7px;
  background-color: #b5b5b5;
}

.button-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

.column-name-div {
  border-radius: 12px;
  padding: 2px;
  text-align: center;
  margin: 10px;
  background-color: #007bff;
  color: rgb(255, 150, 0);
  cursor: pointer;
  text-transform: uppercase;
  height: 40px;
}
</style>