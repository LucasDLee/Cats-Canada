<template>
  <div class="popup-location">
    <h1>{{ cafeData.name }}</h1>
    <p>{{ cafeData.address }}</p>
  </div>
</template>

<script>
export default {
  props: ['cafeData']
}
</script>

<style scoped>
.popup-location {
  min-width: 15vw;
}
</style>
