<template>
  <div>
    <form @submit="changeWordCount">
      <div class="form-group">
        <label for="wordCount" class='make-bold'>Word Count:</label>
        <input
          type="number"
          class="form-control"
          id="wordCount"
          v-model="wordCount"
          placeholder="wordCount"
        />
      </div>
      <button type="submit" class="btn btn-outline-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "WordCountFilter",
  data() {
    return {
      wordCount: "",
    };
  },
  methods: {
    ...mapActions(["text/changeWordCount"]),
    changeWordCount(evt) {
      evt.preventDefault();
      const payload = {
        wordCount: this.wordCount,
      };
      this.$store.dispatch("text/changeWordCount", { payload });
    },
  },
};
</script>

<style scoped>

form {
  width: 60%;
}
</style>