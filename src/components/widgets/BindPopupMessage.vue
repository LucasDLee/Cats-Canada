<template>
  <h1>{{ cafeData.name }}</h1>
  <p>{{ cafeData.address }}</p>
</template>

<script>
export default {
  props: ['cafeData'],
};
</script>