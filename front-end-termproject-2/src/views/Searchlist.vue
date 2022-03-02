<template>
  <br />
  <h1>Search List</h1>
  <hr />
  <br />
  <div class="container-fuild">
    <div class="row">
      <div class="col-6">
        <form @submit.prevent="searchName">
          <h2>Search Name</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <div class="row">
              <div class="col-3"></div>
              <div class="col-6">
                <input
                  class="form-control"
                  type="text"
                  v-model="queryName"
                  placeholder="Recipe input"
                />
              </div>
              <div class="col-3"></div>
            </div>
          </div>
          <button type="submit" class="btn btn-light">Submit</button>
        </form>
      </div>
      <div class="col-6">
        <form @submit.prevent="searchIngredient">
          <h2>Search Ingredients</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <div class="row">
              <div class="col-3"></div>
              <div class="col-6">
                <input
                  class="form-control"
                  type="text"
                  v-model="queryIngredient"
                  placeholder="Ingredients input"
                />
              </div>
              <div class="col-3"></div>
            </div>
          </div>
          <button type="submit" class="btn btn-light">Submit</button>
        </form>
      </div>
    </div>
    <br />
  </div>

  <br />
  <div v-if="queryName">
    <div id="content">
      <br />
      <h4 id="C">Search by Name</h4>
      <SearchName :dataName="item" v-for="item in dataName" :key="item.id" />
    </div>
  </div>
    <div v-if="queryIngredient">
    <div id="content">
      <br />
      <h4 id="C">Search by Ingredient</h4>
      <SearchIngredient :dataIngredient="x" v-for="x in dataIngredient" :key="x.id" />
    </div>
  </div>
</template>

<script>
import Service from "../services/DataService.js";
import SearchName from "../components/SearchName.vue";
import SearchIngredient from "../components/SearchIngredients.vue";
export default {
  name: "Searchlist",
  components: {
    SearchName,
    SearchIngredient
  },
  data() {
    return {
      queryName: "",
      queryIngredient: "",
      dataName: null,
      dataIngredient: null,
    };
  },
  methods: {
    searchName() {
      console.log(this.queryName);
      Service.SearchName(this.queryName)
        .then((response) => {
          this.dataName = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    searchIngredient() {
      console.log(this.queryIngredient);
      Service.SearchIngredient(this.queryIngredient)
        .then((response) => {
          this.dataIngredient = response.data;
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
.col-6 {
  padding: 2%;
}
.container-fuild {
  padding-top: 2%;
  background-color: rgb(77, 85, 185);
  border: 2px solid black;
  border-radius: 20px;
  margin: 2%;
}
#content {
  width: 100;
  background-color: rgb(205, 206, 221);
  border: 2px solid black;
}

#C {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

h1 {
  color: white;
}
</style>
