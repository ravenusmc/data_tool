<template>
  <div>
    <Navbar />

    <section>

      <div>
        <h3 class='login-title center'>Login</h3>
      </div>

      <form @submit="login">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            class="form-control"
            id="username"
            v-model="username"
            placeholder="Enter username"
          />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input
            type="password"
            class="form-control"
            id="exampleInputPassword1"
            v-model="password"
            placeholder="Password"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>

    </section>

    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";
import { mapActions } from "vuex";

export default {
  name: "signup",
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions([ "common/login"]),
    login(evt) {
      evt.preventDefault();
      const payload = {
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch("common/login", { payload });
    },
  },
};
</script>

<style scoped>

section {
  margin: 100px 0 100px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-title {
  text-transform: uppercase;
  color: rgb(0, 125, 225);
}

form {
  border: 2px solid rgb(0, 125, 225);
  background-color: rgba(0, 0, 0, 0.3);
  padding: 30px;
  width: 45%;
}

/****************
Media Queries
****************/

/* Mobile Screen */
@media only all and (max-width: 900px) {

  form {
    border: 2px solid rgb(0, 125, 225);
    background-color: rgba(0, 0, 0, 0.3);
    padding: 30px;
    width: 65%;
  }
}

</style>