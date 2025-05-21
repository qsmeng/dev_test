import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';

// 创建Pinia实例
const pinia = createPinia();
const app = createApp(App);

// 挂载Pinia到Vue应用
app.use(pinia);
app.mount('#app');