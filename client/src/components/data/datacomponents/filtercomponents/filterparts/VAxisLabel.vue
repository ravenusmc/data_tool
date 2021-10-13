<template>
  <div>
    <div>
      <label for="two">V-Axis Label:</label>
      <input type="text" id="title" v-model="vAxisName" />
      <button
        type="submit"
        v-on:click="changeVAxisTitle()"
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
  name: "VAxisLabel",
  data() {
    return {
      vAxisName: "",
    };
  },
  methods: {
    ...mapActions("data", ["changeVAxisName"]),
    changeVAxisTitle() {
      this.changeVAxisName(this.vAxisName);
    },
  },
};
</script>

<style scoped>
.button-fix {
  margin-left: 3%;
}
</style>