import axios from "axios";

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,

  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: localStorage.getItem("token"),
  },
});
export default apiClient;
