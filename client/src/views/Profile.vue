<template>
  <div>
    <section>
      <p>Hi {{ userObject.username }}!</p>
      <button
        class="btn btn-outline-primary"
        v-on:click="showChangePasswordArea()"
      >
        {{ this.changePasswordButtonText }}
      </button>
      <form @submit="submit">
        <div>
          <h3 class="login-title center">Login</h3>
          <!-- <p class="center redText" v-if="passwordNoMatch">
            Password Or Username Invalid
          </p> -->
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
        <div v-if="changePasswordArea">
          <div class="form-group">
            <label for="exampleInputPassword1">Original Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword1"
              v-model="original_password"
              placeholder="Original Password"
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
          <div class="form-group">
            <label for="exampleInputPassword2">Confirm Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword2"
              v-model="password2"
              placeholder="Confirm Password"
            />
          </div>
        </div>

        <button type="submit" class="btn btn-outline-primary">Submit</button>
      </form>
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
      email: "",
      original_password: "",
      password: "",
      password2: "",
    };
  },
  computed: {
    ...mapGetters("session", ["userObject"]),
  },
  methods: {
    submit(evt) {
      evt.preventDefault();
      console.log(this.$store.getters['session/userObject'])
      if (this.username == "") {
        this.username = this.$store.getters['session/userObject'].username
      } else if (this.password != this.password2) {
        alert("Passwords are not the same");
      } else if (this.password.length < 6) {
        alert("Password must be at least 6 characters long");
      } else {
        const payload = {
          username: this.username,
          email: this.email,
          original_password: this.original_password,
          password: this.password,
        };
        console.log(payload);
        // this.$store.dispatch("common/login", { payload });
      }
    },
    showChangePasswordArea() {
      if (this.changePasswordArea == true) {
        this.changePasswordButtonText = "Change Password";
        this.changePasswordArea = false;
      } else {
        this.changePasswordButtonText = "Hide Change Password";
        this.changePasswordArea = true;
      }
    },
  },
};
</script>

<style scoped>
</style>