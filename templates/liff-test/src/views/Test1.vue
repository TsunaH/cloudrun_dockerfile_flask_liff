<script setup>
  import {reactive, ref, useTemplateRef} from "vue";
  import {useRouter} from "vue-router";
  import {useMemberStore} from "../stores/memberStore.js";

  // BackEndの処理呼び出し用
  import axios from "axios";

  // 顧客情報取得用のfunction呼び出し

  let member = ref({
    'name': "1",
    'email': '22',
    'points': 0,
    'note': '333',
  });

/*
  const callapi = async function() {
    try {
      const response = await axios
        .get('/api/apitest')
        //.get('https://cloudrun-dockerfile-flask-liff-973730455124.asia-northeast1.run.app/api/apitest')
      return response.data;
    } catch (error) {
      alert("call api error"+error);
    }
  }
  const member = callapi();
*/
  //  const member = response.data;
  const response = axios.get('/api/apitest');
  const memberInfo = response.data;

//  member.name = memberInfo.name;

  console.log("test henna");
  console.log(JSON.stringify(response));
  console.log(JSON.stringify(member));

//  alert(member.name);
  alert (JSON.stringify(response));
  alert(JSON.stringify(member));

  const router = useRouter();
  const onUpdate = function() {
    console.log("update exec");
    console.log(member);

    const memberStore = useMemberStore();
    memberStore.update(
      member.name,
      member.email,
      member.points,
      member.note
    );
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
        <input type="text" id="inputName" v-model="member.name">
      </dd>
      <dt>
        <label for="inputEmail">メールアドレス&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputEmail" v-model="member.email">
      </dd>
      <dt>
        <label for="inputPoints">ポイント&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputPoints" v-model="member.points">
      </dd>
      <dt>
        <label for="inputNote">備考&nbsp;</label>
      </dt>
      <dd>
        <input type="text" id="inputNote" v-model="member.note">
      </dd>
    </dl>
    <button type="submit">確認</button>
  </form>
</template>