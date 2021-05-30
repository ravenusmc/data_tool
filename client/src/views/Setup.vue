<template>
  <div>

    <section>
      <div class="card" style="width: 30rem">
        <img
          class="card-img-top"
          src="../assets/images/language.jpg"
          alt="Card image cap"
        />
        <div class="card-body">
          <h5 class="card-title">Text Analysis</h5>
          <p class="card-text">
            The user will be able to upload a text document here. The user will
            then be able to analyze it by the most common words and sentiment of
            each sentence as well as the over all sentiment of the document.
          </p>
          <a class="btn btn-primary">
            <router-link class="fontColor font" to="/text_analysis">
              Get Started...
            </router-link>
          </a>
        </div>
      </div>

      <div class="card" style="width: 30rem">
        <img
          class="card-img-top"
          src="../assets/images/graphs.jpg"
          alt="Card image cap"
        />
        <div class="card-body">
          <h5 class="card-title">Data Analysis</h5>
          <p class="card-text">
            The user will be able to upload a csv file here and be able to do
            some basic data analysis on the document
          </p>
          <a class="btn btn-primary">
            <router-link class="fontColor font" to="/data_analysis">
              Get Started...
            </router-link>
          </a>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  name: "Home",
};
</script>

<style scoped>
section {
  margin: 50px 20px 50px 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  grid-gap: 3em;
  justify-items: center;
}

.fontColor {
  color: rgb(255, 150, 0) !important;
}
</style>