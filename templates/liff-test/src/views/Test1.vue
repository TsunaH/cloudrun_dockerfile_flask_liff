<script setup>
  const props = defineProps({
    'name': String,
    'value': String
  })
</script>
  
<template>
  test1です
  <p>{{props.name}}</p>
  <input type="text" v-bind:value="value">
</template>