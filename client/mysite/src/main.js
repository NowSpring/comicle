import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import Antd from "ant-design-vue";

import "ant-design-vue/dist/antd.css";


loadFonts();

const app = createApp(App);

app.use(Antd);
app.use(store);
app.use(router);
app.use(vuetify);
app.mount("#app");