<template>
  <div>
    <section>
      <p>Hi {{ userObject.username }}!</p>
      <!-- <form @submit="login">
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

        <button type="submit" class="btn btn-outline-primary">Submit</button>
      </form> -->
    </section>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "profile",
  computed: {
    ...mapGetters("session", ["userObject"]),
  },
};
</script>

<style scoped>
</style>