<template>
  <div>
    <section>
      <div class="image-div"></div>
      <div>
        <h2 class="center">Background on Data Tool</h2>
        <div class='paragragh-div'>
          <p>
            This project has been in my mind for a while. I wanted to build a
            massive project that would really be able to show off a lot of my
            skills. I started programming almost five years ago. During that
            time I got the idea that I really wanted to focus on data
            visualization. I slowly started to get into it as I learned how to
            program. I was able to reach all of my goals with it. This project
            is the culmination of everything that I've learned.
          </p>
          <p>
            Despite what I say above, the Data Tool is simply a "proof of
            concept". It could have a lot of changes to it - this product is
            very much a MVP.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "DataToolBackGround",
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 50px;
}

.image-div {
  background-image: url("../../assets/images/Dashboard.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  height: 300px;
}

.paragragh-div {
  padding: 20px;
}
</style>