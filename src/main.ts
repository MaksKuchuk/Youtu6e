import { createApp } from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';
import './index.css';

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
});

createApp(App).use(store).use(router).mount('#app');
