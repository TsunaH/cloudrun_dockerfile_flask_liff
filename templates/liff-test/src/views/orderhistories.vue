<script setup>
  import {getLineId} from "../util/common.js";
  import {constvalue} from "../util/const.js";

  import {ref} from "vue";
  // BackEndの処理呼び出し用
  import axios from "axios";

  // 履歴データ取得
  let orderhistories = ref("");
  let control_items = ref("");

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
        orderhistories.value = result.data.data;
        control_items.value = result.data.control_items;
        //alert("in then");
        //alert(JSON.stringify(result));
        // エラーの場合
        alert(JSON.stringify(orderhistories.value));
      })
    }
</script>
  
<template>
  <form v-on:submit.prevent="onUpdate">
    <dl>
      <div
        v-for="orderhistory in orderhistories"
        v-bind:key="KEY"
        style="border: 1px solid #333333;"> 
        <dt v-if="control_items.order_id==constvalue['DISP_ONLY']">■注文番号&nbsp;</dt>
        <dd v-if="control_items.order_id==constvalue['DISP_ONLY']">&nbsp;&nbsp;{{orderhistory.order_id}}</dd>
        <dt v-if="control_items.order_regist_day==constvalue['DISP_ONLY']">■注文日&nbsp;</dt>
        <dd v-if="control_items.order_regist_day==constvalue['DISP_ONLY']">&nbsp;&nbsp;{{orderhistory.order_regist_day}}</dd>
        <dt v-if="control_items.product_infos==constvalue['DISP_ONLY']">■ご注文商品（数量）&nbsp;</dt>
          <div
            v-for="product_info in orderhistory.product_infos"
            v-bind:key="KEY"
            v-if="control_items.product_infos==constvalue['DISP_ONLY']">
            &nbsp;&nbsp;{{ product_info.product_name }}({{ product_info.order_qty }})
          </div>
        <dt v-if="control_items.order_amount==constvalue['DISP_ONLY']">■ご注文金額&nbsp;</dt>
        <dd v-if="control_items.order_amount==constvalue['DISP_ONLY']">&nbsp;&nbsp;{{orderhistory.order_amount}}</dd>
        <dt v-if="control_items.shipment_detail_status==constvalue['DISP_ONLY']">■ご注文の状態&nbsp;</dt>
        <dd v-if="control_items.shipment_detail_status==constvalue['DISP_ONLY']">&nbsp;&nbsp;{{orderhistory.shipment_detail_status}}</dd>
      </div>
    </dl>
  </form>
</template>