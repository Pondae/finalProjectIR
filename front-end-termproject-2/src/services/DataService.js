import apiClient from "./AxiosClient.js";

export default {
  SearchName(query) {
    return apiClient.post("/title_name", {
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
