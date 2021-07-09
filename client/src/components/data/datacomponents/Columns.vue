<template>
  <div>
    <div>
      <h3>Columns</h3>
      <div
        v-for="column in columns"
        :key="column.index"
        class="column-name-div"
      >
        <p>{{ column.name }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Columns",
  computed: {
    ...mapGetters("data", ["columns"]),
  },
  data() {
    return {
      books: [
        {
          id: 0,
          name: "one",
        },
        {
          id: 1,
          name: "two",
        },
      ],
    };
  }, // End of Data
};
</script>

<style scoped>
.column-name-div {
  border: 2px solid red;
  padding: 5px;
  text-align: center;
  margin: 10px;
}
</style>