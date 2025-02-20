<script setup>
  import {reactive, ref, useTemplateRef} from "vue";
  import {useRouter} from "vue-router";
  import {useMemberStore} from "../stores/memberStore.js";
  import {useLineStore} from "../stores/lineStore.js";
  import liff from "@line/liff";


  // BackEndの処理呼び出し用
  import axios from "axios";

  userId = 
  liff.getProfile()
  .then(
    function(profile) {
      userId = profile.userId; 
    }
  )

  // 顧客情報取得用のfunction呼び出し

  let member = ref({
    'name': "1",
    'email': '22',
    'points': 0,
    'note': '333',
  });


  const callapi = async function() {
    let response;
    try {
      lineStore = useLineStore()
      lineId = lineStore.getId()
      response = await axios
        .post(
          '/api/apitest',
          {
              lineid: lineId
          })
        //.get('https://cloudrun-dockerfile-flask-liff-973730455124.asia-northeast1.run.app/api/apitest')
        .then(function(result) {
          member.value = result.data;
          alert("in then");
          alert(JSON.stringify(result));
          alert(JSON.stringify(member.value));
        })
    } catch (error) {
      alert("call api error"+error);
    }
    return response;
  }
  callapi();

  alert("test henna");
  alert(JSON.stringify(member.value));

  const router = useRouter();
  const onUpdate = function() {
    console.log("update exec");
    console.log(member.value);

    const memberStore = useMemberStore();
    memberStore.update(
      member.value.name,
      member.value.email,
      member.value.points,
      member.value.note
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