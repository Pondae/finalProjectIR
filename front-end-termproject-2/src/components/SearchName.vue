<template>
  <br />
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
  />
  <div class="col">
    <div class="card" style="100">
      <div class="card-body">
        <span>
          <div>
            <div class="row">
              <div class="col-4">
                <img
                  class="img-responsive"
                  style="width: 100%"
                  :src="'FoodImages/' + dataName.Image"
                />
              </div>
              <div class="col-8">
                <div class="row">
                  <div class="col-6">
                    <h4>
                      Food Title: <span id="title">{{ dataName.Title }}</span>
                    </h4>
                  </div>
                  <div class="col-6" id="check">
                    <div v-if="!checked">
                      <h7 id="mark">mark</h7>
                      <input
                        v-if="!checked"
                        type="checkbox"
                        id="checkbox"
                        v-model="checked"
                        @input="AddData"
                      />
                    </div>
                    <h7 id="mark">unmark</h7>
                    <input
                      type="checkbox"
                      id="checkbox"
                      v-model="checked"
                      @input="AddData"
                    />
                  </div>
                </div>
                <h5 class="card-title"></h5>
                <p class="card-text">
                  {{ dataName.Recipe }}
                </p>
              </div>
            </div>
          </div>
        </span>
      </div>
      <br />
      <br />
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
      checked: false,
    };
  },
  methods: {
    AddData() {
      console.log(this.image);
      var myObj = {
        title: this.dataName.Title,
        recipe: this.dataName.Recipe,
      };
      if (this.checked === false) {
        this.GStore.Keepdata.push(myObj);
        console.log(this.checked);
        console.log("hi");
      }
      if (this.checked === true) {
        this.GStore.Keepdata.pop();
        console.log(this.checked);
        console.log("hi");
      }
      console.log(this.GStore.Keepdata);
    },
  },
  created() {},
};
</script>

<style scoped>
#mark {
  padding-right: 2%;
}
#checkbox {
  padding-right: 3%;
}
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
