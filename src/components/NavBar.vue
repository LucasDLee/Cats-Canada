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
  background-color: var(--hyperlink-bg-color);
  text-transform: uppercase;
  text-align: center;
  font-weight: 600;
}

nav > * {
  display: inline-block;
  list-style: outside none none;
  margin: 0 1em;
  padding: 0;
}

nav > * {
  padding: 0.7em 0.7em;
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
  transition: all .35s ease;
  opacity: 0;
}

nav > *::before {
  content: '';
  right: 0;
  top: 0;
  border-top: 3px solid #3E8914;
  border-right: 3px solid #2E640F;
  transform: translate(-100%, 50%);
}

nav > *:after {
  content: '';
  left: 0;
  bottom: 0;
  border-bottom: 3px solid #2E640F;
  border-left: 3px solid #3E8914;
  transform: translate(100%, -50%)
}

nav > *:hover:before,
nav > *:hover:after{
  transform: translate(0,0);
  opacity: 1;
}

nav > *:hover {
  color: #3DA35D;
}
</style>
