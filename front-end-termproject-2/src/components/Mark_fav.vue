<template>
  <br />
  <div class="col">
    <div class="card" style="100">
      <div class="card-body">
        <span>
          <div>
            <h4>
              Food Title: <span id="title">{{ fav_data.Title }}</span>
            </h4>
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
  name: "Mark_fav",
  props: {
    fav_data: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {};
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
