<template>
  <div>
    <section>
      <div class="file-upload-area">
        <h1 class="center paragraph-title">PURPOSE</h1>
        <p class="purpose-paragraph">
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
            class="test"
          />
        </div>
        <button
          type="submit"
          class="btn btn-outline-primary"
        >
          Submit
        </button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
	name: "FileArea",
};
</script>

<style scoped>
</style>