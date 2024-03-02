import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import Test from "../views/Test.vue";
import ComicMaster from "../views/ComicMaster.vue";
import ComicVersion from "../views/ComicVersion.vue";


const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/comicmaster",
    name: "comicmaster",
    component: ComicMaster,
    meta: { requiresAuth: true },
    children: [
      {
        path: "comicversion/:id", 
        name: "comicversion",
        component: ComicVersion,
        props: true, 
        meta: { requiresAuth: true },
      }
    ]
  },
  {
    path: "/test",
    name: "test",
    component: Test,
  },
];

const router = createRouter({
  history: process.env.IS_ELECTRON
    ? createWebHashHistory()
    : createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  if (to.meta.requiresAuth && window.localStorage.getItem("token") === null) {
    return { name: "login" };
  }
});

export default router;
