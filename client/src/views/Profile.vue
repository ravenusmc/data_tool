<template>
  <div>
    <section>
      <form @submit="submit">
        <div>
          <h2 class="center name-greeting">
            Welcome {{ userObject.username }}!
          </h2>
          <h3 class="login-title center">Change User Information</h3>
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
        <div>
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
            <label for="exampleInputPassword1">New Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword1"
              v-model="password"
              placeholder="New Password"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputPassword2">Confirm New Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword2"
              v-model="password2"
              placeholder="Confirm New Password"
            />
          </div>
        </div>

        <button type="submit" class="btn btn-outline-primary">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import axios from "axios";

export default {
  name: "profile",
  data() {
    return {
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
    async submit(evt) {
      evt.preventDefault();

      if (this.username == "") {
        this.username = this.$store.getters["session/userObject"].username;
      }

      if (this.email == "") {
        this.email = this.$store.getters["session/userObject"].email;
      }

      const passwordCheck = {
        id: this.$store.getters["session/userObject"].id,
        originalPassword: this.original_password,
      };

      const result = await axios.post(
        "http://localhost:5000/check_password",
        passwordCheck
      );

      if (result.data == false) {
        alert("Original Password is invalid");
      } else if (this.password != this.password2) {
        alert("Passwords are not the same");
      } else if (this.password.length < 6) {
        alert("Password must be at least 6 characters long");
      } else {
        const payload = {
          id: this.$store.getters["session/userObject"].id,
          username: this.username,
          email: this.email,
          originalPassword: this.original_password,
          password: this.password,
        };
        this.$store.dispatch("session/updateUserProfile", { payload });
      }
    },
  },
};
</script>

<style scoped>
.change-password-btn {
  margin-bottom: 50px;
}

.name-greeting {
  text-transform: uppercase;
}

section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-title {
  text-transform: uppercase;
  color: rgb(0, 125, 225);
}

form {
  border: 2px solid rgb(0, 125, 225);
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 15px;
  padding: 30px;
  width: 45%;
}
</style>