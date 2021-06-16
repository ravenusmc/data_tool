<template>
  <div>
    <section>
      <p>Hi {{ userObject.username }}!</p>

      <form @submit="submit">
        <div>
          <h3 class="login-title center">Login</h3>
          <p class="center redText" v-if="passwordNoMatch">
            Password Or Username Invalid
          </p>
        </div>

        <div class="form-group">
          <label for="username">Username</label>
          <input
            class="form-control"
            id="username"
            v-model="username"
            :placeholder="userObject.username"
          />
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">Email address</label>
          <input
            type="email"
            class="form-control"
            id="exampleInputEmail1"
            v-model="email"
            aria-describedby="emailHelp"
            :placeholder="userObject.email"
          />
        </div>
        <div>
          <div class="form-group" v-if="changePasswordArea">
            <label for="exampleInputPassword1">Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword1"
              v-model="password"
              placeholder="Password"
            />
          </div>
        </div>

        <button type="submit" class="btn btn-outline-primary">Submit</button>
      </form>
      <button
        class="btn btn-outline-primary"
        v-on:click="showChangePasswordArea()"
      >
        {{ this.changePasswordButtonText }}
      </button>
    </section>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "profile",
  data() {
    return {
      changePasswordArea: false,
      changePasswordButtonText: "Change Password",
      username: "",
    };
  },
  computed: {
    ...mapGetters("session", ["userObject"]),
  },
  methods: {
    submit(evt) {
      evt.preventDefault();
      const payload = {
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch("common/login", { payload });
    },
    showChangePasswordArea() {
      if (this.changePasswordArea == true) {
        this.changePasswordButtonText = "Change Password";
        this.changePasswordArea = false;
      } else {
        this.changePasswordButtonText = "Hide Change Password";
        this.changePasswordArea = true;
      }
      console.log("hi");
    },
  },
};
</script>

<style scoped>
</style>