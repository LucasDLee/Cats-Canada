<template>
  <v-container fluid id="about-view">
    <div class="about">
      <section>
        <h1>About the Website</h1>
        <p>Ever wanted to find cat cafes in Canada? Well, now you can thanks to the Cat Map!</p>
        <p>The website lists and logs the names and addresses of all organizations that have set up a cat
          cafe in Canada.</p>
      </section>

      <section>
        <h1>Contact</h1>
        <p>If you don't see your organization on the map, feel free to contact me to send me an email at <a href="mailto:lucasdlee23@gmail.com?subject=Cats Canada Inquiry">lucasdlee23@gmail.com</a>.</p>
      </section>
    </div>
    <AboutFooter />
  </v-container>
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

.about>section {
  margin: 1em 0;
}

.about>section p {
  margin: 0.5em 0;
}
</style>
