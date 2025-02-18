<script setup>
  import liff from "@line/liff";
  import {useMemberStore} from "../stores/memberStore.js";
  import axios from "axios";

  const memberStore = useMemberStore();

  const onUpdate = function() {
    console.log("登録ボタン押下");

    const response = axios.get('/api/apitest');
    alert(response);

    liff
      .sendMessages([
      {
        type: "text",
        text: "Hello, World!",
      },
      ])
      .then(() => {
        alert("message sent");
      })
      .catch((err) => {
        alert("error", err);
      });
  }
</script>
  
<template>
  test2です
  <form v-on:submit.prevent="onUpdate">
    <dl>
      <dt>
        <label for="inputName">名前&nbsp;</label>
      </dt>
      <dd>
        {{memberStore.name}}
      </dd>
      <dt>
        <label for="inputEmail">メールアドレス&nbsp;</label>
      </dt>
      <dd>
        {{memberStore.email}}
      </dd>
      <dt>
        <label for="inputPoints">ポイント&nbsp;</label>
      </dt>
      <dd>
        {{memberStore.points}}
      </dd>
      <dt>
        <label for="inputNote">備考&nbsp;</label>
      </dt>
      <dd>
        {{memberStore.note}}
      </dd>
    </dl>
    <button type="submit">登録</button>
  </form>
</template>