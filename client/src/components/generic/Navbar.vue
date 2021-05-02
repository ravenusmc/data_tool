<template>
  <div>
    <!-- BootStrap Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light backgroundColor">
      <a class="navbar-brand fontColor font" href="#">Data Tool</a>
      <button
        class="navbar-toggler"
        style="color: #fff"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#"
              ><router-link class="fontColor font" to="/">Home</router-link></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"
              ><router-link class="fontColor font" to="/set_up">Set up</router-link></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"
              ><router-link class="fontColor font" to="/login">Login</router-link></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"
              ><router-link class="fontColor font" to="/sign_up">Sign Up</router-link></a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"
              ><router-link class="fontColor font" to="/about"
                >About</router-link
              ></a
            >
          </li>
        </ul>
      </div>
    </nav>
    <!-- End BootStrap Navbar -->
  </div>
</template>

<script>
export default {};
</script>

<style scoped>

.backgroundColor {
  background-color: rgb(0, 125, 225) !important;
}
.fontColor {
  color: rgb(225, 100, 0) !important;
}
.navbar-toggler {
  background-color: white;
}

</style>