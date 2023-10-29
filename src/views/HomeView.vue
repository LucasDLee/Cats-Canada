<template>
  <section class="contents">
    <l-map
      id="cat-map"
      ref="map"
      v-model:zoom="zoom"
      :center="mapCenter"
      :max-bounds="bounds"
      @mousemove="getCoords"
    >
      <l-control-layers position="topright"></l-control-layers>
      <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        layer-type="base"
      />

      <l-geo-json 
        refs="cafes"
        :geojson="cafesList"
        @click="onFeatureClick">
      </l-geo-json>

      <l-control-scale position="bottomleft"></l-control-scale>

      <div class="mouseOverCoord">
        <span class="info--text">{{ this.mouseLatLon.lat }}</span>, 
        <span class="info--text">{{ this.mouseLatLon.lon }}</span>
      </div>
    </l-map>
  </section>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import { LMap, LGeoJson, LTileLayer, LControlScale, LControlLayers } from '@vue-leaflet/vue-leaflet'

export default {
  async created () {
    const cafes = await fetch('./static/json/cafes.geojson')
    this.cafesList = await cafes.json()
  },
  components: {
    LControlLayers,
    LControlScale,
    LGeoJson,
    LMap,
    LTileLayer
  },
  data() {
    return {
      bounds: [
        [90, 0],
        [90, -180],
        [35, 0],
        [35, -180]
      ],
      cafesList: null,
      mapCenter: [54.5, -94],
      mouseLatLon: {
        lat: 0,
        lon: 0
      },
      tileProviders: [
        {
          name: 'ESRI World Street Map',
          visible: true,
          url: 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
          attribution: '&copy; <a href="https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/">ESRI World Street M</a>'
        },
        {
          name: 'OpenStreetMap',
          visible: false,
          attribution:
            '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        },
        {
          name: 'Wikimedia Maps',
          visible: false,
          url: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png',
          attribution: '&copy; <a href="https://www.mediawiki.org/wiki/Wikimedia_Maps/API">Wikimedia Maps API</a>'
        }
      ],
      zoom: 5
    }
  },
  methods: {
    getCoords: function (event) {
      this.mouseLatLon.lat = event.latlng.lat.toFixed(4)
      this.mouseLatLon.lon = event.latlng.lng.toFixed(4)
    },
    onFeatureClick: function (e) {
      const properties = e.layer.feature.properties
      this.mapCenter = [this.mouseLatLon.lat, this.mouseLatLon.lon]
      e.sourceTarget.bindPopup(`<b>Name:</b> ${properties.name}<br><b>Address:</b> ${properties.address}<br><b>Province:</b> ${properties.province}`).openPopup()
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
