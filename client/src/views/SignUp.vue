<template>
  <div>

    <section>

      <form @submit="submitSelection">

        <div>
          <h3 class='login-title center'>Sign Up</h3>
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
          <label for="exampleInputEmail1">Email address</label>
          <input
            type="email"
            class="form-control"
            id="exampleInputEmail1"
            v-model="email"
            aria-describedby="emailHelp"
            placeholder="Enter email"
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
          <label for="exampleInputPassword2">Retype Password</label>
          <input
            type="password"
            class="form-control"
            v-model="password_confirm"
            id="exampleInputPassword2"
            placeholder="Retype Password"
          />
        </div>
        <button type="button" class="btn btn-outline-primary">Submit</button>
      </form>

    </section>

  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "signup",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password_confirm: "",
    };
  },
  methods: {
		...mapActions([ "common/setUpUser"]),
    submitSelection(evt) {
      evt.preventDefault();
      if (this.username == '') {
        alert('Uername must be entered');
      }else if (this.email == '') {
        alert('Email must be entered');
      }else if (this.password != this.password_confirm) {
        alert('Passwords Must be the Same');
      }else if (this.password.length <6) {
        alert('Password must be at least 6 characters long')
      } else {
      const payload = {
        email: this.email,
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch("common/setUpUser", { payload });
      }

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
  border-radius: 15px;
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