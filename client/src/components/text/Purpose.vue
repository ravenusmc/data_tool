<template>
  <div>
    <section>
      <div>
        <h1 class="center">PURPOSE</h1>
        <p>
          The purpose of this page is to all the user to upload a text document
          to do some sentiment analysis on it. The page will allow the user to
          see the overall sentiment of the document, the sentiment by sentence
          as well as a graph of the most common words in the document. How this
          works:
          <br />
          <br />
          <span>1.</span> Simply upload a text (.txt) document.
          <br />
          <span>2.</span> The application will do the rest and show you the data
          about your document below.
        </p>
      </div>

      <div class="file-upload-area">
        <div class="input-area">
          <input
            type="file"
            id="file"
            ref="file"
            name="file"
            v-on:change="handleFileUpload()"
          />
        </div>
        <button
          type="submit"
          v-on:click="submitFile()"
          class="btn btn-outline-primary"
        >
          Submit
        </button>
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
      file: "",
    };
  }, // End of Data
  methods: {
    ...mapActions(["text/handleFileUpload"]),
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      this.$store.dispatch("text/handleFileUpload", { formData });
    },
  }, // End of Methods
};
</script>

<style scoped>
section {
  margin: 50px 50px 50px 50px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 3em;
  justify-items: center;
}

.file-upload-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  background-color: rgba(0, 0, 0, 0.2);
}

.input-area {
  display: grid;
  margin-left: 15%;
}

span {
  font-weight: bold;
}

button {
  margin-top: 30px;
}

/****************
Media Queries
****************/

/* Mobile Screen */
@media only all and (max-width: 900px) {

  .file-upload-area {
    height: 275px;
  }

}
</style>