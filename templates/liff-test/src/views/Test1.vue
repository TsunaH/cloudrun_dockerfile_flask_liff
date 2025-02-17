<script setup>
  import {reactive} from "vue";
  import {useRouter} from "vue-router";
  import {useMemberStore} from "../stores/memberStore.js";

  // BackEndの処理呼び出し用
  import axios from "axios";

  // 顧客情報取得用のfunction呼び出し
  var memberStore = await axios.get('https://cloudrun-dockerfile-flask-liff-973730455124.asia-northeast1.run.app/api/apitest');
console.log(memberStore);

alert(memberStore.name);
alert(memberStore);

  const router = useRouter();
  const onUpdate = function() {
    console.log("update exec");
    console.log(memberStore);
    useMemberStore.update(memberStore)
    router.push({name: "Test2"});
  }
</script>
  
<template>
  test1です
  <form v-on:submit.prevent="onUpdate">
    <dl>
      <dt>
        <label for="inputName">名前&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputName" v-model="memberStore.name">
      </dd>
      <dt>
        <label for="inputEmail">メールアドレス&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputEmail" v-model="memberStore.email">
      </dd>
      <dt>
        <label for="inputPoints">ポイント&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputPoints" v-model="memberStore.points">
      </dd>
      <dt>
        <label for="inputNote">備考&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputNote" v-model="memberStore.note">
      </dd>
    </dl>
    <button type="submit">確認</button>
  </form>
</template>