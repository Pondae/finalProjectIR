<template>
  <br />
  <div class="col">
    <div class="card" style="100">
      <div class="card-body">
        <span>
          <div>
            <div class="row">
              <div class="col-6">
                <h4>
                  Food Title: <span id="title">{{ fav_data.Title }}</span>
                </h4>
              </div>
              <div class="col-6" id="check">
                <div v-if="!checked">
                  <h7 id="mark">unmark</h7>
                  <input
                    v-if="!checked"
                    type="checkbox"
                    id="checkbox"
                    v-model="checked"
                    @input="AddData"
                  />
                </div>
                <h7 id="mark">mark</h7>
                <input
                  type="checkbox"
                  id="checkbox"
                  v-model="checked"
                  @input="AddData"
                />
              </div>
            </div>
          </div>
          <h5 class="card-title"></h5>
          <p class="card-text">
            {{ fav_data.Recipe }}
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
  name: "Mark_fav",
  props: {
    fav_data: {
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
      var myObj = {
        id : this.fav_data.id
      };
      if (this.checked === false) {
        this.GStore.Deldata.push(myObj);
        console.log(this.checked);
      }
      if (this.checked === true) {
        this.GStore.Deldata.pop();
        console.log(this.checked);
      }
      console.log(this.GStore.Deldata);
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
  background-color: rgb(149, 179, 207);
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
