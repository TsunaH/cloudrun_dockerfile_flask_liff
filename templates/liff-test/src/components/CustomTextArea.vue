<script setup>

const props = defineProps({
  'name': String,
  'value': String
})
</script>

<template>
  <p>{{props.name}}</p>
  <input type="text" v-bind:value="value">
</template>