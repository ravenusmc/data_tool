<template>
  <div>
    <section>
      <button
        class="btn btn-outline-primary change-password-btn"
        v-on:click="showChangePasswordArea()"
      >
        {{ this.changePasswordButtonText }}
      </button>
      <form @submit="submit">
        <div>
          <h2 class='center name-greeting'>Hi {{ userObject.username }}!</h2>
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
      if (this.username == "") {
        this.username = this.$store.getters["session/userObject"].username;
      }

      if (this.email == "") {
        this.email = this.$store.getters["session/userObject"].email;
      }

      if (this.password != this.password2) {
        alert("Passwords are not the same");
      } else if (this.password.length < 6) {
        alert("Password must be at least 6 characters long");
      } else {
        const payload = {
          id: this.$store.getters["session/userObject"].id,
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