import { createApp } from 'vue';
import App from './App.vue';

import liff from "@line/liff";

createApp(App).mount('#app');

liff
  .init({
    //liffId: liffid, // Use own liffId
    liffId: "2006831755-QEdgjOA8",
  });