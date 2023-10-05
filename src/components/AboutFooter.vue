<template>
  <footer id="about-footer">
    <a :href="githubProfile" target="_blank">
      <img :src="githubImg" width="50" height="50" alt="github" />
    </a>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      githubProfile: 'https://github.com/LucasDLee',
      githubImg: '/img/github.webp'
    }
  }
}
</script>

<style scoped>
#about-footer {
  background-color: aqua;
  bottom: 0;
  display: flex;
  flex-direction: row;
  left: 0;
  padding: 0.75rem 0;
  position: absolute;
  width: 100vw;
}
</style>
