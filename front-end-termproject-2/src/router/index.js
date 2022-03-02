import { createRouter, createWebHistory } from "vue-router";
import Searchlist from "../views/Searchlist.vue";
import Login from "../views/Login.vue";
const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/",
    name: "Searchlist",
    component: Searchlist,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
