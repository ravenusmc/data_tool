<template>
  <div>
    <section>
      <form class="change-username-form" @submit="changeUsernameAndEmail">
        <div>
          <h2 class="center name-greeting">
            Welcome {{ userObject.username }}!
          </h2>
          <h3 class="login-title center">Change User Information</h3>
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
        <button type="submit" class="btn btn-outline-dark">Submit</button>
      </form>

      <form @submit="changePassword">
        <div>
          <h3 class="login-title center">Change Password</h3>
        </div>
        <div class="form-group">
          <label for="exampleInputPassword">Original Password</label>
          <input
            type="password"
            class="form-control"
            id="exampleInputPassword"
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
        <button type="submit" class="btn btn-outline-dark">Submit</button>
      </form>
      <form @submit="deleteUser" class="delete-user">
        <button type="submit" class="btn btn-outline-danger">
          Delete User
        </button>
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
    ...mapActions(["session/updateUserProfile"]),
    changeUsernameAndEmail(evt) {
      evt.preventDefault();

      if (this.username == "") {
        this.username = this.$store.getters["session/userObject"].username;
      }

      if (this.email == "") {
        this.email = this.$store.getters["session/userObject"].email;
      }

      const payload = {
        id: this.$store.getters["session/userObject"].id,
        username: this.username,
        email: this.email,
        password: "",
      };
      this.$store.dispatch("session/updateUserProfile", { payload });
    }, // End changeUsernameAndEmail
    async changePassword(evt) {
      evt.preventDefault();

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
          password: this.password,
        };
        this.$store.dispatch("session/updateUserProfile", { payload });
      }
    }, // End changePassword
    deleteUser(evt) {
      evt.preventDefault();
      const payload = {
        id: this.$store.getters["session/userObject"].id,
      };
      this.$store.dispatch("session/deleteUser", { payload });
    },
  },
};
</script>

<style scoped>
.change-username-form {
  margin-bottom: 30px;
}
.change-password-btn {
  margin-bottom: 50px;
}

.name-greeting {
  text-transform: uppercase;
}

section {
  margin: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-title {
  text-transform: uppercase;
  color: #333;
}

form {
  border: 2px solid rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 15px;
  padding: 30px;
  width: 45%;
}

.delete-user {
  border: 2px solid red;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
}
</style>