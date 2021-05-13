<template>
  <div>
    <section>
      <div>
        <h1 class="center">Purpose</h1>
        <p>
          The purpose of this page is to all the user to upload a text document
          to do some sentiment analysis on it. The page will allow the user to
          see the overall sentiment of the document, the sentiment by sentence
          as well as a graph of the most common words in the document.
        </p>
      </div>

      <div>
        <div class="container">
          <div class="large-12 medium-12 small-12 cell">
            <label
              >File
              <input
                type="file"
                id="file"
                ref="file"
                name='file'
                v-on:change="handleFileUpload()"
              />
            </label>
            <button v-on:click="submitFile()">Submit</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
	name: "Purpose",
	data() {
		return {
			file: '',
		}
	}, // End of Data
  methods: {
    ...mapActions([ "text/handleFileUpload"]),
    handleFileUpload() {
			this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);
      // let payload = this.file
      this.$store.dispatch("text/handleFileUpload", { formData })
    },
  }, // End of Methods
};
</script>

<style scoped>
section {
  margin: 50px 30px 50px 30px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  grid-gap: 3em;
  justify-items: center;
  border: 2px solid red;
}
</style>