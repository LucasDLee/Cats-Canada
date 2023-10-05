<template>
  <section class="contents">
    <l-map
      id="cat-map"
      ref="map"
      v-model:zoom="zoom"
      :center="[54.5, -94]"
      :max-bounds="bounds"
      @mousemove="getCoords"
    >
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
      ></l-tile-layer>

      <l-control-scale position="bottomleft"></l-control-scale>

      <div class="mouseOverCoord">
        <span class="info--text">{{ this.mouseLatLon.lat }}</span
        >, <span class="info--text">{{ this.mouseLatLon.lon }}</span>
      </div>
    </l-map>
  </section>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import { LMap, LTileLayer, LControlScale } from '@vue-leaflet/vue-leaflet'

export default {
  components: {
    LMap,
    LTileLayer,
    LControlScale
  },
  data() {
    return {
      bounds: [
        [90, 0],
        [90, -180],
        [0, 0],
        [0, -180]
      ],
      mouseLatLon: {
        lat: 0,
        lon: 0
      },
      zoom: 5
    }
  },
  methods: {
    getCoords: function (event) {
      this.mouseLatLon.lon = event.latlng.lng.toFixed(4)
      this.mouseLatLon.lat = event.latlng.lat.toFixed(4)
    }
  }
}
</script>

<style scoped>
.mouseOverCoord {
  background-color: black;
  border-radius: 15px;
  color: #aad3df;
  bottom: 4em;
  left: 0.5em;
  padding: 0.5em;
  position: absolute;
  z-index: 10000;
}
</style>
