import { createRouter, createWebHistory } from "vue-router";
import Searchlist from "../views/Searchlist.vue";
import SearchAS from "../views/SearchAS.vue";
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
  {
    path: "/searchAS",
    name: "SearchAS",
    component: SearchAS,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
