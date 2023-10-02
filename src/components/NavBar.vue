<template>
  <nav>
    <RouterLink to="/">Cat Map</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
nav {
  background-color: aliceblue;
  border-bottom: 1px dotted black;
  display: flex;
  gap: 0 1em;
  flex-direction: row;
  padding: 1em;
  height: 2vh;
}

nav>* {
  color: hsla(160, 100%, 37%, 1);
  font-size: 20px;
  text-decoration: none;
}

nav>*:hover {
  font-style: italic;
}
</style>