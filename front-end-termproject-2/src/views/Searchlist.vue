<template>
  <br />
  <h1>Search List</h1>
  <hr />
  <br />
  <div class="container-fuild">
    <div class="row">
      <div class="col-6">
        <form @submit.prevent="searchTFIDF">
          <h2>Search Recipe</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <div class="row">
              <div class="col-3"></div>
              <div class="col-6">
                <input
                  class="form-control"
                  type="text"
                  v-model="queryTF"
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
        <form @submit.prevent="searchTF">
          <h2>Search ingredients</h2>
          <br />
          <div class="form-group">
            <label for="exampleInputPassword1">Qurey:</label>
            <div class="row">
              <div class="col-3"></div>
              <div class="col-6">
                <input
                  class="form-control"
                  type="text"
                  v-model="queryTF"
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
  <div>
    <br />
    <div v-if="queryTFIDF">
      <h4 id="TFIDF">TFIDF</h4>
      <SearchTFIDF
        :dataTF_IDF="item"
        v-for="item in dataTF_IDF"
        :key="item.id"
      />
    </div>
    <div v-if="queryTF">
      <h4 id="TF">TF</h4>
      <SearchTF :dataTF="x" v-for="x in dataTF" :key="x.id" />
    </div>
    <div v-if="querybm25">
      <h4 id="BM25">BM25</h4>
      <SearchBM2 :dataBM25="k" v-for="k in dataBM25" :key="k.id" />
    </div>
  </div>
</template>

<script>
import Service from "../services/DataService.js";
import SearchTFIDF from "../components/SearchTFIDF.vue";
import SearchTF from "../components/SearchTF.vue";
import SearchBM2 from "../components/SearchBM25.vue";
export default {
  name: "Searchlist",
  components: {
    SearchTFIDF,
    SearchTF,
    SearchBM2,
  },
  data() {
    return {
      queryTF: "",
      queryTFIDF: "",
      querybm25: "",
      dataTF: null,
      dataTF_IDF: null,
      dataBM25: null,
    };
  },
  methods: {
    searchTFIDF() {
      console.log(this.queryTFIDF);
      Service.searchTFIDF(this.queryTFIDF)
        .then((response) => {
          this.dataTF_IDF = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    searchTF() {
      console.log(this.queryTFIDF);
      Service.searchTF(this.queryTF)
        .then((response) => {
          this.dataTF = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    bm25() {
      console.log(this.querybm25);
      Service.searchBM25(this.querybm25)
        .then((response) => {
          this.dataBM25 = response.data;
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

.col-6 {
  padding: 2%;
}
.container-fuild {
  padding-top: 2%;
  background-color: rgb(196, 198, 230);
  border: 2px solid black;
  border-radius: 20px;
  margin: 2%;
}
#TFIDF {
  color: white;
}
#TF {
  color: white;
}
#BM25 {
  color: white;
}

h1 {
  color: white;
}
</style>
