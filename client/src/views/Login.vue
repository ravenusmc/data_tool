<template>
  <div>
    <section>
      <form @submit="login">
        <div>
          <h3 class="login-title center">Login</h3>
          <p class="center redText" v-if="passwordNoMatch">
            Password Or Username Invalid
            {{ this.passwordNoMatch }}
          </p>
          <p class="center redText" v-if="notFound">
            User has not signed up.
            <a
              ><router-link class="redText fontColor font" to="/sign_up"
                >Please sign up.</router-link
              ></a
            >
          </p>
        </div>

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

        <button type="submit" class="btn btn-outline-dark">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "signup",
  computed: {
    ...mapGetters("common", ["passwordNoMatch", "notFound"]),
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["common/login"]),
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-title {
  text-transform: uppercase;
  color: #333;
}

form {
  border: 2px solid rgb(0, 0, 0);
  border-radius: 15px;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 30px;
  width: 45%;
}

.fontColor:hover {
  color: #333 !important;
}

/****************
Media Queries
****************/

/* Mobile Screen */
@media only all and (max-width: 900px) {
  form {
    width: 70%;
  }
}
</style>