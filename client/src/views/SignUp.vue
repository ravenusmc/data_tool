<template>
  <div>
    <div>
      <h3>Sign Up</h3>
    </div>

    <section>
      <form @submit="submitSelection">
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
            placeholder="Password"
          />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Retype Password</label>
          <input
            type="password"
            class="form-control"
            id="exampleInputPassword1"
            placeholder="Retype Password"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  name: "signup",
  data() {
    return {
			email: "",
			username: "",
    };
  },
  methods: {
    submitSelection(evt) {
      evt.preventDefault();
      console.log(this.username);
      // if (this.yearOne < 1963){
      //   alert('The first year must be greater than 1962!')
      // }else if (this.yearTwo > 2013){
      //   alert('The second year must not be greater than 2013!')
      // }else if (this.yearOne >= this.yearTwo){
      //   alert('The first year must be less than the second year!')
      // }else if (this.yearTwo <= this.yearOne){
      //   alert('The second year must be greater than the first year!')
      // }else if ( ((this.yearTwo - this.yearOne) > 5) && this.years) {
      // 	alert('Plesae do NOT Search for more than a five year time span!')
      // }else if (this.vehicle == ""){
      // 	alert('Please select a vehicle!')
      // }
      // else {
      // 	const payload = {
      // 		vehicle: this.vehicle,
      // 		yearOne: this.yearOne,
      // 		yearTwo: this.yearTwo,
      // 		useYears: this.years
      // 	};
      // 	this.$store.dispatch('eva/fetchVehicleInformation', { payload })
      // }
    },
  },
};
</script>

<style scoped>
form {
  width: 50%;
}
</style>