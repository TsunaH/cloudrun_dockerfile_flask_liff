<script setup>
  import {getLineId} from "../util/common.js";
  import {constvalue} from "../util/const.js";

  import {ref} from "vue";
  // BackEndの処理呼び出し用
  import axios from "axios";

  // 履歴データ取得
  let orderhistories = ref("");

  // データ取得処理呼び出し
  getData();

  /**
   * 注文履歴データ取得処理
   */
  async function getData() {
    // LINE ID取得
    const lineId = await getLineId()

    axios
      .post(
        constvalue['API_GET_ORDERHISTORIES'],
        {
            lineId: lineId
        })
      .then(function(result) {
        // データ処理が正常の場合
        orderhistories.value = result.data;
        alert("in then");
      alert(JSON.stringify(result));
        // エラーの場合
        alert(JSON.stringify(orderhistories.value));
      })
    }
</script>
  
<template>
  <form v-on:submit.prevent="onUpdate">

    <dl>
      <template
        v-for="orderhistory in orderhistories"
        v-bind:key="KEY"> 
        <dt>■注文番号&nbsp;</dt>
        <dd>&nbsp;&nbsp;{{orderhistory.order_id}}</dd>
        <dt>注文日&nbsp;</dt>
        <dd>{{orderhistory.email}}</dd>
        <dt>■ご注文商品（数量）&nbsp;</dt>
          <template
            v-for="product_info in orderhistory.product_infos"
            v-bind:key="KEY">
            {{ product_info.product_name }}({{ product_info.order_qty }})
          </template>
        <dt>■ご注文金額&nbsp;</dt>
        <dd>&nbsp;&nbsp;{{orderhistory.order_amount}}</dd>
        <dt>■ご注文の状態&nbsp;</dt>
        <dd>&nbsp;&nbsp;{{orderhistory.shipment_detail_status}}</dd>
      </template>
    </dl>
  </form>
</template>