<template>
  <nav class="navbar">
    <router-link to="/" class="nav-link">
      <h5 id="meal">Search Meal</h5>
    </router-link>
    <div class="columnn">
      <span style="font-weight: bold; margin-right: 2%">
        {{GStore.currentUser}}
      </span>

      <button class="btn btn-logout-color" @click="logout" style="color: white">
        Logout
      </button>
    </div>
  </nav>

  <div>
    <router-view />
  </div>
</template>

<script>
export default {
  inject: ["GStore"]
};
</script>

<style>
#inline {
  display: inline-block;
  margin-right: 10px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-image: url("../src/assets/background.png");
  height: 100%;
  margin: 0;
}

body,
html {
  height: 100%;
  margin: 0;
}

.navbar {
  padding: 10px;
  text-align: end;
  background-color: #030853;
}

.page-layout {
  padding: 0 50px 0 50px;
}
#meal {
  color: white;
}
.columnn {
  margin: 0.4% 0 auto 0;
  float: left;
  width: 50%;
  color: white;
}
</style>
