<template>
  <div>
    <section>
      <div class="file-upload-area">
        <h1 class="center paragraph-title">PURPOSE</h1>
        <p class="purpose-paragraph">
          The purpose of this page is to all the user to upload a csv document
          and then to be able to see some basic data visualizations. How this
          works:
          <br />
          <br />
          <span>1.</span> Simply upload a csv (.csv) document.
          <br />
          <span>2.</span> The application will set up all the fields so that the
          user will be able to make their own graph
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
  name: "FileArea",
  data() {
    return {
      file: "",
    };
  }, // End of Data
  methods: {
    ...mapActions(["data/fetchFileInformation"]),
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      this.$store.dispatch("data/fetchFileInformation", { formData });
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

.paragraph-title {
  padding-top: 2%;
}

.purpose-paragraph {
  padding: 3%;
}

.file-upload-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  background-color: #f5f5f5;
  box-shadow: 8px 8px 15px black;
  border: 2px solid rgb(0, 0, 0);
}

.input-area {
  display: grid;
  margin-left: 20%;
}

span {
  font-weight: bold;
}

button {
  margin-top: 30px;
}

label {
  border: 2px solid red;
}

label:hover {
  background-color: blue;
}

input[type="file"]::file-selector-button {
  border: 2px solid #6c5ce7;
  padding: 0.2em 0.4em;
  border-radius: 0.2em;
  background-color: #a29bfe;
  transition: 1s;
}

input[type="file"]::file-selector-button:hover {
  background-color: #81ecec;
  border: 2px solid #00cec9;
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