<template>
  <div>
    <div class="h-axis-fix">
      <label for="two">H-Axis Label:</label>
      <input type="text" id="title" v-model="hAxisName" />
      <button
        type="submit"
        v-on:click="changeHAxisTitle()"
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
  name: "HAxisLabel",
  data() {
    return {
      hAxisName: "",
    };
  },
  methods: {
    ...mapActions("data", ["changeHAxisName"]),
    changeHAxisTitle() {
      this.changeHAxisName(this.hAxisName);
    },
  },
};
</script>

<style scoped>
.button-fix {
  margin-left: 3%;
}

.h-axis-fix {
  margin-bottom: 2%;
}
</style>