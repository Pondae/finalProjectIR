import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import GStore from "./store";

createApp(App).provide("GStore", GStore).use(router).mount("#app");
