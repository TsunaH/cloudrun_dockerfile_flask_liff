import { createApp } from 'vue';
import App from './App.vue';

import liff from "@line/liff";

// ローカルテスト用
//let liffid = "2006831755-QxVm4KvW";
// LINE動作確認要
let liffid = "2006831755-QEdgjOA8";

liff
  .init({
    liffId: liffid, // Use own liffId
  })
  .then(() => {
    liff.sendMessages([
    {
      type: "text",
      text: "Hello World"
    }
    ]);
  });

createApp(App).mount('#app');
