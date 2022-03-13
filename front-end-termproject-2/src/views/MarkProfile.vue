<template>
  <div class="fav_data">
    <br />
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
    />
    <div class="container-fuild">
      <div class="row">
        <div class="col-4">
          <img id="image" src="../assets/Guess.png" />
        </div>
        <div class="col-4"><img id="image" src="../assets/Guess2.png" /></div>
        <div class="col-4"><img id="image" src="../assets/Guess3.png" /></div>
      </div>
    </div>
    <br />
    <div>
      <form @submit.prevent="searchfav">
        <h2 style="color: white">Search</h2>
        <br />
        <div class="form-group">
          <label for="exampleInputPassword1">Qurey:</label>
          <div class="row">
            <div class="col-3"></div>
            <div class="col-6">
              <input
                class="form-control"
                type="text"
                v-model="query"
                placeholder="Title input"
              />
            </div>
            <div class="col-3" id="left">
              <button type="submit" class="btn btn-light">search</button>
            </div>
          </div>
        </div>
      </form>
    </div>
    <br />
    <div v-if="!query">
      <div id="content">
        <br />
        <form @submit.prevent="unmarktoDatabase">
          <div class="butt">
            <button type="submit" class="btn btn-light">UNMARK</button>
          </div>
          <Mark :fav_data="i" v-for="i in fav_data" :key="i.id" />
        </form>
      </div>
    </div>
    <div v-if="query">
      <Searchfav :search_data="x" v-for="x in search_data" :key="x.id" />
    </div>
  </div>
</template>

<script>
import Service from "../services/DataService.js";
import Mark from "../components/Mark_fav.vue";
import Searchfav from "../components/SearchMark.vue";
export default {
  inject: ["GStore"],
  name: "MarkProfile",
  components: {
    Mark,
    Searchfav,
  },
  data() {
    return {
      fav_data: null,
      query: "",
      search_data: null,
      data: null,
      id: null,
      userid: null
    };
  },
  methods: {
    searchfav() {
      console.log(this.query);
      this.userid = this.GStore.currentUserid
      Service.SearchFav(this.query,this.userid)
        .then((response) => {
          this.search_data = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    unmarktoDatabase() {
      this.data = this.GStore.Deldata;
      console.log(this.data);
      this.GStore.Deldata = [];
      this.data.forEach((element) => {
        Service.UnMarktoData(element);
      });
      this.$router.push({ name: "Searchlist" });
    },
  },
  created() {
    this.id = this.GStore.currentUserid
    console.log(this.id)
    Service.Get_MarktoData(this.id)
      .then((response) => {
        this.fav_data = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
.butt {
  text-align: right;
  padding-right: 1.5%;
  padding-bottom: 2%;
}
#image {
  width: 100%;
  border-radius: 50px;
  border: solid 3px rgb(0, 0, 0);
  text-align: left;
}

.fav_data {
  background-color: rgb(139, 167, 209);
  width: 100%;
  height: 100%;
}
body,
html {
  height: 100%;
}
.col-4 {
  padding-left: 2%;
  padding-right: 2%;
}
#left {
  text-align: left;
}
</style>
