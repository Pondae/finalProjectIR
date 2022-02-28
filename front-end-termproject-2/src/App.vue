<template>
  <nav class="navbar">
    <router-link to="/searchAS" class="nav-link">
      <h5 id="AS">Search Artist & Search Songname</h5>
    </router-link>
    <router-link to="/" class="nav-link">
      <h5 id="AS">Search Vector</h5>
    </router-link>
  </nav>

  <div>
    <router-view />
  </div>
</template>

<script>
export default {};
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
#AS {
  color: white;
}
</style>
