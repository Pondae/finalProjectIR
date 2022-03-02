import apiClient from "./AxiosClient.js";

export default {
  SearchName(query) {
    console.log('searchname')
    return apiClient.post("/title_name", {
      query: query,
    });
  },
  SearchIngredient(query) {
    console.log('searchIngredient')
    return apiClient.post("/ingredients", {
      query: query,
    });
  },
  Login(data) {
    console.log(data)
    console.log(data.username)
    console.log(data.password)
    return apiClient.post("/Login", {
      username: data.username,
      password: data.password
    });
  },
};
