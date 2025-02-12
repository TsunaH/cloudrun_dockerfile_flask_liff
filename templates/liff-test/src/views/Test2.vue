<script setup>
  import {useMemberStore} from "../stores/memberStore"

  const memberStore = useMemberStore();

  const onUpdate = function() {
    console.log("登録ボタン押下");
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