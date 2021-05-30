<template>
  <div>
    
      <section>
        <div class='title-div'>
          <h1 class='title_header'>Data Tool</h1>
        </div>
      </section>
  </div>
</template>

<script>


export default {
  name: "Home",
};

</script>

<style scoped>

section {
  background-image: url('../assets/images/landing.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
	height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title_header {
  font-size: 6rem;
  font-weight: 600;
  letter-spacing: -.3rem;
  color: rgb(225, 100, 0);
}

.title-div {
  background-color: rgba(0, 125, 225, 0.8);
  padding: 20px;
}

</style>
