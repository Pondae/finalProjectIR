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
          <h5 class="card-title"></h5>
           <h4>SongName:</h4>
          <h4 class="card-text">
            
            {{ dataArtist.Songname }}
          </h4>
        </span>
        <br />
        <br />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Searchresult",
  props: {
    dataArtist: {
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
  letter-spacing: 1px;
  display: inline-block;
  border-radius: 60px;
  transition: 0.5s;
  background-size: cover;
  position: relative;
}
</style>
