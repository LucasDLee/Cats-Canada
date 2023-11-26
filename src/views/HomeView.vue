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
        <l-popup><BindPopupMessage :cafeData=selectedCafeProperties></BindPopupMessage></l-popup>
      </l-geo-json>

      <l-control-scale position="bottomleft"></l-control-scale>

      <div class="mouseOverCoord">
        <span class="info--text">{{ this.mouseLatLon.lat }}</span>, 
        <span class="info--text">{{ this.mouseLatLon.lon }}</span>
      </div>
    </l-map>
    <div class="locations">
      <section 
        v-for="(cafeObject, cafeId) in cafesListDetails"
        :key="cafeId">
        <h1>{{ cafeObject.properties.name }}</h1>
        <p>{{ cafeObject.properties.address }}</p>
        <p>{{ cafeObject.properties.province }}</p>
      </section>
    </div>
  </section>
</template>

<script>
import BindPopupMessage from '@/components/widgets/BindPopupMessage.vue'
import 'leaflet/dist/leaflet.css'
import { LMap, LPopup, LGeoJson, LTileLayer, LControlScale, LControlLayers } from '@vue-leaflet/vue-leaflet'

export default {
  async created () {
    const cafes = await fetch('./static/json/cafes.geojson')
    this.cafesList = await cafes.json()
    this.cafesListDetails = this.cafesList.features
  },
  components: {
    BindPopupMessage,
    LControlLayers,
    LControlScale,
    LGeoJson,
    LMap,
    LPopup,
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
      cafesListDetails: null,
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
          attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
        },
        {
          name: 'OpenStreetMap',
          visible: false,
          url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
          attribution:'&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        },
        {
          name: 'Stadia Maps',
          visible: false,
          url: 'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
          attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        },
        {
          name: 'Wikimedia Maps',
          visible: false,
          url: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png',
          attribution: '&copy; <a href="https://www.mediawiki.org/wiki/Wikimedia_Maps/API">Wikimedia Maps API</a>'
        }
      ],
      selectedCafeProperties: '',
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
      this.selectedCafeProperties = properties
    }
  }
}
</script>

<style scoped>
.contents {
  width: 100vw;
  /* height: 94.5vh; */
  display: flex;
  /* grid-template-columns: auto auto; */
  flex-direction: row;
  height: 75vh;
  padding: 1em;
}

.locations {
  background-color: green;
}
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
