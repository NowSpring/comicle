import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import ComicMaster from "../views/ComicMaster.vue";
import ComicVersion from "../views/ComicVersion.vue";
import ComicEpisode from "../views/ComicEpisode.vue";
import Test from "../views/Test.vue";


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
        path: ":id/comicversion", 
        name: "comicversion",
        component: ComicVersion,
        props: true, 
        meta: { requiresAuth: true },
        children: [
          {
            path: ":id/comicepisode", 
            name: "comicepisode",
            component: ComicEpisode,
            props: true, 
            meta: { requiresAuth: true },
          }
        ]
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
