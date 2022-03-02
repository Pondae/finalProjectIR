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
          <span
            ><h4>SongName:</h4>
            <h5>{{ dataTF.Songname }}</h5></span
          >
          <h5 class="card-title"></h5>
          <p class="card-text">
            {{ dataTF.Lyric }}
          </p>
        </span>
        <br />
        <br />
        <h5>ARTIST: {{ dataTF.artist }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Searchresult",
  props: {
    dataTF: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.card {
  background-color: rgb(224, 234, 255);
}
.col-4 {
  padding: 2%;
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
</style>
