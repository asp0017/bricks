import Vue from "vue";
import VueRouter from "vue-router";
import Bricks from "../components/BricksTest.vue";

Vue.use(VueRouter);

const routes = [
  //測試連線
  {
    path: "/bricks",
    name: "BricksTest",
    component: Bricks,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
