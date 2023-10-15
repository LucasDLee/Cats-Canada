<template>
  <div class="about">
    <h1>About the Website</h1>
    <p>Ever wanted to find cat cafes in Canada? Well, now you can thanks to the Cat Map!</p>
    <p>
      The website lists and logs the names and addresses of all organizations that have set up a cat
      cafe in Canada.
    </p>
    <p>Why?</p>
    <p>Because I like cats.</p>

    <h1>Contacts</h1>
    <p>If you don't see your organization on the map, feel free to contact me</p>
  </div>
  <AboutFooter />
</template>

<script setup>
import AboutFooter from '@/components/AboutFooter.vue'
</script>

<style>
.about {
  display: flex;
  flex-direction: column;
  padding: 1em;
}
</style>
