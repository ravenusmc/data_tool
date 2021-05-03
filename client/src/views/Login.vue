<template>
  <div>
    <Navbar />

    <div>
      <h3>Login</h3>
    </div>

    <section>
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
form {
  width: 50%;
}
</style>