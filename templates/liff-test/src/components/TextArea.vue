<script setup>

const props = defineProps({
  'name': String,
  'value': String
})
</script>

<template>
  <section>
      <div>■{{ props.name }}</div>
      <input type="text" v-model="props.value">
  </section>
</template>