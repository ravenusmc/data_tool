<template>
  <div>
    <section>
      <div class="x-axis">
        <h6>X-Axis:</h6>
        <draggable
          @onDrop="onDrop"
          :list="arrXAxis"
          ghost-class="moving-card"
          group="columnNames"
        >
          <div v-for="column in arrXAxis" :key="column.index">
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
      <draggable :list="startColumns" group="columnNames">
        <div
          v-for="column in startColumns"
          :key="column.index"
          :id="column.index"
          class="column-name-div card"
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
    ...mapGetters("data", ["columns"]),
  },
  data() {
    return {
      startColumns: this.$store.getters["data/columns"],
      arrXAxis: [],
      arrYAxis: [],
    };
  }, // End of Data
  methods: {
    onDrop: function (event) {
      console.log("HI");
    },
  },
  // mounted() {
  //   let startColumns = this.$store.getters["data/columns"];
  // },
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