import { createRouter, createWebHistory } from "vue-router";
import Searchlist from "../views/Searchlist.vue";
import Login from "../views/Login.vue";
import MarkProfile from "../views/MarkProfile.vue";
const routes = [
  {
    path: "/markProfile",
    name: "MarkProfile",
    component: MarkProfile,
  },
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
