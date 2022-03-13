<template>
  <br />
  <br />
  <br />
  <div class="container">
    <div class="row">
      <div class="col-4"></div>
      <div class="col-4">
        <form @submit.prevent="onLogin">
          <h2>Login</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Username:</label>
            <input
              class="form-control"
              type="text"
              placeholder="input username"
              v-model="username"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password:</label>
            <input
              type="password"
              class="form-control"
              id="exampleInputPassword1"
              placeholder="input password"
              v-model="password"
            />
          </div>
          <button type="submit" class="btn btn-light">Submit</button>
        </form>
      </div>
      <div class="col-4"></div>
    </div>
  </div>
</template>

<script>
import Service from "../services/DataService.js";
export default {
  name: "Searchlist",
  inject: ["GStore"],
  components: {},
  data() {
    return {
      username: "",
      password: "",
      checked: null,
    };
  },

  methods: {
    onLogin() {
      let data = {
        username: this.username,
        password: this.password,
      };
      Service.Login(data)
        .then((response) => {
          this.GStore.currentUserid = response.data[0].userid;
          this.GStore.currentUser = response.data[0].user;
          this.checked = response.data[0].check;
          console.log(this.checked);
          if (this.checked == true) {
            this.$router.push({
              name: "Searchlist",
            });
          } else {
            location.reload();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {},
};
</script>

<style scoped>
body,
html {
  height: 100%;
  margin: 0;
}
.container {
  margin-top: 5%;
  /* top right bottom left */
  color: black;
  padding: 2% 70px 70px 100px;
  background-color: rgb(196, 198, 230);
  border: 2px solid black;
  border-radius: 25px;
  height: 100%;
}
</style>
