<template>
  <div>
    <section>
      <h3 class="center">Columns</h3>
      <div
        v-for="column in columns"
        :key="column.index"
        :id="column.index"
        class="column-name-div card"
      >
        <p>{{ column.name }}</p>
      </div>
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
  props: ["id", "draggable"],
  methods: {
    add() {
      if (this.newTask) {
        this.arrXAxis.push({ name: this.newTask });
        this.newTask = "";
      }
    },
  },
  data() {
    return {
      newTask: "",
      arrXAxis: [],
      arrYAxis: [],
    };
  }, // End of Data
};
</script>

<style scoped>
section {
  border: 2px solid black;
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