var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2)

const {createApp} = Vue

const app = createApp({
    data() {
        return {
            map: null,
            themeList: window.themeList,
            fixedLayers: window.fixedLayers,
            overlayList: window.overlayList,
            satteliteList: window.satteliteList,
            maxZoom: 8,
            bounds: window.bounds,
        }
    },
    methods: {
        initMap() {
            this.map = L.map('map', {
                    maxZoom: this.maxZoom,
                    zoomControl: false,
                    layers: [
                        this.themeList[0].geolyr, this.themeList[0].geolyr,
                        this.fixedLayers[0].geolyr,
                        this.fixedLayers[1].geolyr,
                        this.overlayList[0].geolyr,
                    ]
                }
            ).fitBounds(this.bounds)
            var zoomHome = L.Control.zoomHome()
            zoomHome.addTo(this.map)
        },
        activeThemeLayer(id) {
            this.satteliteList.forEach((layer) => {
                this.map.removeLayer(layer.geolyr)
                layer.active = false
                return layer
            })

            this.themeList.find(layer => {
                this.map.addLayer(this.fixedLayers[0].geolyr)
                this.map.addLayer(this.fixedLayers[1].geolyr)
                if (layer.id === id) {
                    layer.active = true
                    this.map.addLayer(layer.geolyr)
                } else {
                    layer.active = false
                    this.map.removeLayer(layer.geolyr)
                }
            })
        },
        activeOverlayLayer(id) {
            this.overlayList.find(layer => {
                if (layer.id === id) {
                    layer.active = !layer.active
                    if (layer.active) {
                        this.map.addLayer(layer.geolyr)
                    } else {
                        layer.active = false
                        this.map.removeLayer(layer.geolyr)
                    }
                }
            })
        },
        activeSatteliteLayer(id) {
            this.satteliteList.find(layer => {
                if (layer.id === id) {
                    layer.active = true
                    this.map.addLayer(layer.geolyr)
                    this.map.removeLayer(this.fixedLayers[0].geolyr)
                    this.map.removeLayer(this.fixedLayers[1].geolyr)
                    this.themeList.forEach((layer) => {
                        this.map.removeLayer(layer.geolyr)
                        layer.active = false
                        return layer
                    })
                } else {
                    layer.active = false
                    this.map.removeLayer(layer.geolyr)
                }
            })
        },
    },
    mounted() {
        this.initMap()
    }
    ,
})

// Delimiters changed to ES6 template string style
app.config.compilerOptions.delimiters = ['${', '}']
app.mount('#app')
