<script setup>
  import {reactive} from "vue";
  import {useRouter} from "vue-router";
  import {useMemberStore} from "../stores/memberStore.js";

  // BackEndの処理呼び出し用
  import axios from "axios";

  // 顧客情報取得用のfunction呼び出し
  //const response = await axios.get('https://cloudrun-dockerfile-flask-liff-973730455124.asia-northeast1.run.app/api/apitest');
  const response = await axios.get('/api/apitest');
  const member = response.data;

  console.log("test henna");
  console.log(member);

  alert(member.name);
  alert(member);

  const router = useRouter();
  const onUpdate = function() {
    console.log("update exec");
    console.log(this.member);

    const memberStore = useMemberStore();
    useMemberStore.update(member)
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
        <input type="text" id="inputName" v-bind:value="member.name">
      </dd>
      <dt>
        <label for="inputEmail">メールアドレス&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputEmail" v-bind:value="member.email">
      </dd>
      <dt>
        <label for="inputPoints">ポイント&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputPoints" v-bind:value="member.points">
      </dd>
      <dt>
        <label for="inputNote">備考&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputNote" v-bind:value="member.note">
      </dd>
    </dl>
    <button type="submit">確認</button>
  </form>
</template>