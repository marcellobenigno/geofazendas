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
            maxZoom: 20,
            bounds: window.bounds,
            estados: [],
            municipios: [],
            estadoSelecionado: '',
            municipioSelecionado: [],
            municipioLayer: null
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
        getEstados() {
            axios.get(estadosURL)
                .then((response) => {
                    this.estados = response.data;
                })
                .catch(resonse => {
                    console.log('error')
                })
        },
        getMunicipios(event) {
            axios.get(municipiosURL, {params: {estado: this.estadoSelecionado, no_page: 'no_page'}})
                .then((response) => {
                    this.municipios = response.data;
                })
                .catch(resonse => {
                    console.log('error')
                })
        },
        getMunicipioSelecionado(event) {
            if (this.municipioLayer !== null){
                this.map.removeLayer(this.municipioLayer)
            }
            let municipio = this.municipios.find(x => x.id === this.municipioSelecionado);
            this.municipioLayer = L.tileLayer.wms(
                window.geoServerUrl, {
                    format: 'image/png',
                    transparent: true,
                    version: '1.1.0',
                    maxZoom: 20,
                    opacity: 1,
                    zIndex: 5,
                    layers: 'geofazendas:mapas_municipio_selecionado',
                    cql_filter: `municipio_id=${municipio.id}`,
                })
            this.map.fitBounds(municipio.extent)
            this.map.addLayer(this.overlayList[1].geolyr)
            this.overlayList[1].active = true
            this.map.addLayer(this.municipioLayer)
        }
    },
    mounted() {
        this.initMap()
        this.getEstados()
        //console.log(this.$refs.id_geoserver_url.value)
    },
    computed: {}
})

// Delimiters changed to ES6 template string style
app.config.compilerOptions.delimiters = ['${', '}']
app.mount('#app')

// https://codesandbox.io/s/chain-select-with-vuejs-2zv2o?from-embed=&file=/src/App.vue:771-789