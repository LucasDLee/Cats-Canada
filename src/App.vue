<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <main>
    <NavBar />

    <RouterView />
  </main>
</template>

<style>
:root {
  --hyperlink-bg-color: #f5f57a;
  --main: #f5f57a;
  --main2: rgb(191, 183, 111, 0.75);
  --main3: #3da35d;
  --main4: rgb(125, 113, 170, 0.67);
  --main5: rgb(128, 125, 106, 0.5);
}

html {
  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    'Fira Sans',
    'Droid Sans',
    'Helvetica Neue',
    sans-serif;
}
</style>