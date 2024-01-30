<template>
  <nav class="bg-green-lighten-3">
    <RouterLink to="/">Cat Map</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
nav {
  border-bottom: 1px dotted black;
  display: flex;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  /* text-align: center; */
  font-weight: 600;
  height: 5vh;
}

nav > * {
  color: #7d71aa;
  display: inline-block;
  list-style: outside none none;
  margin: 0 1em;
  padding: 0;
}

nav > * {
  padding: 0.35em 0.35em;
  position: relative;
  text-decoration: none;
  font-size: 20px;
}

nav > *::before,
nav > *::after {
  content: '';
  height: 14px;
  width: 14px;
  position: absolute;
  transition: all 0.35s ease;
  opacity: 0;
}

nav > *::before {
  content: '';
  right: 0;
  top: 0;
  border-top: 3px solid var(--nav-hover);
  border-right: 3px solid var(--nav-hover);
  transform: translate(-100%, 50%);
}

nav > *:after {
  content: '';
  left: 0;
  bottom: 0;
  border-bottom: 3px solid var(--nav-hover);
  border-left: 3px solid var(--nav-hover);
  transform: translate(100%, -50%);
}

nav > *:hover:before,
nav > *:hover:after {
  transform: translate(0, 0);
  opacity: 1;
}

nav > *:hover {
  color: var(--nav-hover);
}
</style>
