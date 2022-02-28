<template>
  <br />
  <h1>Search List</h1>
  <br />
  <div class="container">
    <div class="row">
      <div class="col-6">
        <form @submit.prevent="searchsongname">
          <h2>Search Songname</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <input
              class="form-control"
              type="text"
              v-model="querysongname"
              placeholder="Songname like rainy day"
            />
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div class="col-6">
        <form @submit.prevent="searchArtist">
          <h2>Search Artist</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <input
              class="form-control"
              type="text"
              v-model="queryArtist"
              placeholder="Artist input"
            />
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </div>
  <div>
    <br />
    <div v-if="queryArtist">
      <SongfromArt
        :dataArtist="item"
        v-for="item in dataArtist"
        :key="item.id"
      />
    </div>
    <div v-if="querysongname">
      <LyricformSong
        :datasongname="item"
        v-for="item in datasongname"
        :key="item.id"
      />
    </div>
  </div>
</template>

<script>
import Service from "../services/DataService.js";
import LyricformSong from "../components/LyricformSong.vue";
import SongfromArt from "../components/SongfromArt.vue";
export default {
  name: "Searchlist",
  components: {
    SongfromArt,
    LyricformSong,
  },
  data() {
    return {
      querysongname: "",
      queryArtist: "",
      dataArtist: null,
      datasongname: null,
    };
  },

  methods: {
    searchsongname() {
      console.log(this.querysongname);
      Service.searchsongname(this.querysongname)
        .then((response) => {
          this.datasongname = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    searchArtist() {
      console.log(this.queryArtist);
      Service.searchArtist(this.queryArtist)
        .then((response) => {
          this.dataArtist = response.data;
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
#Searchresult {
  /* margin: 2%; */
}
.btn-add-color {
  background-color: #2b6bcc;
  color: white;
  font-size: 16px;
  padding: 15px;
  border-radius: 25px;
  border: 0;
  cursor: pointer;
}
.col-4 {
  background-color: rgb(111, 156, 223);
}
.container {
  padding-top: 2%;
}
</style>
