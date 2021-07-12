<template>
  <div>
    <section>
      <div class="x-axis">
        <h6>X-Axis:</h6>
        <draggable
          v-model="XAxisArray"
          group="columnNames"
          @change="log"
        >
          <div
            v-for="column in XAxisArray"
            :key="column.index"
            :id="column.index"
          >
            {{ column.name }}
          </div>
        </draggable>
      </div>
      <div class="x-axis">
        <h6>Y-Axis:</h6>
        <draggable
          :list="arrYAxis"
          ghost-class="moving-card"
          group="columnNames"
        >
          <div v-for="column in arrYAxis" :key="column.index">
            {{ column.name }}
          </div>
        </draggable>
      </div>
      <button type="submit" class="btn btn-outline-primary">Make Graph</button>

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
import { mapGetters } from "vuex";
import draggable from "vuedraggable";

export default {
  name: "Columns",
  components: {
    draggable,
  },
  computed: {
    ...mapGetters("data", ["columns", "XAxisArray", "initialColumns"]),
    XAxisArray: {
      get() {
        return this.$store.state.data.XAxisArray;
      },
      set(value) {
        this.$store.dispatch("data/updateXAxis", value);
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
    initialColumns: {
      get() {
        return this.$store.state.data.initialColumns;
      },
      set(value) {
        this.$store.dispatch("data/updateInitialColumns", value);
      },
    },
  },
  data() {
    return {
      // startColumns: this.$store.getters["data/columns"],
      arrXAxis: [],
      arrYAxis: [],
    };
  }, // End of Data
  methods: {
    log: function (event) {
      // console.log(event);
      // console.log(this.arrXAxis);
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
  border: 2px solid black;
}

.x-axis {
  border: 2px solid red;
  height: 80px;
}

.column-name-div {
  border: 2px solid #007bff;
  padding: 2px;
  text-align: center;
  margin: 10px;
  background-color: #007bff;
  color: rgb(255, 150, 0);
  cursor: pointer;
}
</style>