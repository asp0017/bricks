import Vue from "vue";
import VueRouter from "vue-router";
import Bricks from "../components/BricksTest.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import HomePage from "../components/Homepage.vue";

Vue.use(VueRouter);


const routes = [
  //測試連線
  {
    path: "/bricks",
    name: "BricksTest",
    component: Bricks,
  },
  {
    path: "/register",
    name: "RegisterRegister",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/homepage",
    name: "Homepage",
    component: HomePage,
  },
];


const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});


export default router;

