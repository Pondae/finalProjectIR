<template>
  <br />
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
  />
  <div class="col">
    <!-- {{GStore.Keepdata[0][0]}} -->
    <div class="card" style="100">
      <div class="card-body">
        <span>
          <div>
            <div class="row">
              <div class="col-6">
                <h4>
                  Food Title: <span id="title">{{ dataName.Title }}</span>
                </h4>
              </div>
              <div class="col-6" id="check">
                <input type="checkbox" @input="AddData" />
              </div>
            </div>
          </div>
          <h5 class="card-title"></h5>
          <p class="card-text">
            {{ dataName.Recipe }}
          </p>
        </span>
        <br />
        <br />
      </div>
    </div>
  </div>
  <br />
</template>

<script>
export default {
  inject: ["GStore"],
  name: "SearchName",
  props: {
    dataName: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      unique: [],
    };
  },
  methods: {
    AddData() {
      var myObj = {
        "title": this.dataName.Title, //your artist variable
        "recipe": this.dataName.Recipe, //your title variable
      };
      this.GStore.Keepdata.push(myObj);
      // console.log(this.GStore.Keepdata);
    },
  },
  created() {},
};
</script>

<style scoped>
#check {
  text-align: right;
  font: 3em;
}
.card {
  background-color: rgb(154, 160, 231);
}

.card-text {
  text-decoration: none;
  font-family: "Raleway", sans-serif;
  text-transform: lowercase;
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 1px;
  display: inline-block;
  border-radius: 60px;
  transition: 0.5s;
  background-size: cover;
  position: relative;
}
#title {
  color: rgb(221, 230, 255);
  font: 0.8em sans-serif;
  text-transform: uppercase;
}
.card-body {
  text-align: left;
  font-family: Arial, Helvetica, sans-serif;
  font: 0.9em;
}
</style>
