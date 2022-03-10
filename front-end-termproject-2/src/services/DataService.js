import apiClient from "./AxiosClient.js";

export default {
  inject: ["GStore"],
  Move() {
    return this.$router.reload();
  },
  UnMarktoData(data) {
    return apiClient.post("/unmark_data", {
      id: data.id,
    });
  },
  MarktoData(data) {
    return apiClient.post("/mark_data", {
      title: data.title,
      recipe: data.recipe,
      image: data.image
    });
  },
  Get_MarktoData() {
    return apiClient.get("/get_mark_data");
  },
  SearchFav(query) {
    console.log("SearchFav");
    return apiClient.post("/mark_search", {
      query: query,
    });
  },
  SearchName(query) {
    console.log("searchname");
    return apiClient.post("/title_name", {
      query: query,
    });
  },
  SearchIngredient(query) {
    console.log("searchIngredient");
    return apiClient.post("/ingredients", {
      query: query,
    });
  },
  Login(data) {
    console.log(data);
    console.log(data.username);
    console.log(data.password);
    return apiClient.post("/Login", {
      username: data.username,
      password: data.password,
    });
  },
};
