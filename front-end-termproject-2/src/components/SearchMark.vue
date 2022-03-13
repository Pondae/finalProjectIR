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
                  :src="'FoodImages/' + search_data.Image"
                />
              </div>
              <div class="col-8">
                <div class="row">
                  <div class="col-6">
                    <h4>
                      Food Title: <span id="title">{{ search_data.Title }}</span>
                    </h4>
                  </div>
                  <div class="col-6"></div>
                </div>
                <h5 class="card-title">Ingredients</h5>
                <p class="card-text">
                  {{ search_data.Ingredients }}
                </p>
                <br />
                <h5 class="card-title">Recipe</h5>
                <p class="card-text">
                  {{ search_data.Recipe }}
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
  name: "SearchMark",
  props: {
    search_data: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      checked: false,
    };
  },
  methods: {},
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
