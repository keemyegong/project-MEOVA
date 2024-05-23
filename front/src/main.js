import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
const app = createApp(App);
const pinia = createPinia();

app.use(router);
pinia.use(piniaPluginPersistedstate);
app.use(pinia);

app.mount("#app");
