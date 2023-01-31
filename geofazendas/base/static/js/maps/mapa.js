var geoServerUrl = $('#geoserver_url').val() + 'geofazendas/wms?'

var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2)

var overlays = [
    {'id': 1, 'title': 'Estados', 'geolyr': estado, active: true},
    {'id': 2, 'title': 'Municípios', 'geolyr': municipio, active: false},
    {'id': 3, 'title': 'Assentamentos', 'geolyr': assentamento, active: false},
    {'id': 4, 'title': 'Área Indígena', 'geolyr': areaIndigena, active: false},
    {'id': 5, 'title': 'Área Protegida', 'geolyr': areaProtegida, active: false},
    {'id': 6, 'title': 'Isoietas', 'geolyr': isoietas, active: false},
]

var themeList = [
    {'id': 1, 'title': 'Acidez (pH) do Solo a 30-60cm', 'geolyr': phSolo, active: true},
    {'id': 2, 'title': 'Biomas', 'geolyr': bioma, active: false},
    {'id': 3, 'title': 'Capacidade de Água Disponível (AWC)', 'geolyr': capAguaDisp, active: false},
    {'id': 4, 'title': 'Clima', 'geolyr': clima, active: false},
    {'id': 5, 'title': 'Condutividade Elétrica do Solo', 'geolyr': CondutividadeEletrica, active: false},
    {'id': 6, 'title': 'Declividade', 'geolyr': declividade, active: false},
    {'id': 7, 'title': 'Geologia', 'geolyr': geologia, active: false},
    {'id': 8, 'title': 'Geomorfologia', 'geolyr': geomorfologia, active: false},
    {'id': 9, 'title': 'Saturação por Sódio do Solo a 30-100cm', 'geolyr': saturacaoSodio, active: false},
    {'id': 10, 'title': 'Solos', 'geolyr': solo, active: false},
    {'id': 11, 'title': 'Teor de Areia do Solo a 30-60cm', 'geolyr': areiaDisponivelSolo, active: false},
    {'id': 12, 'title': 'Teor de Argila do Solo a 30-60cm', 'geolyr': argilaSolo, active: false},
    {'id': 13, 'title': 'Teor de Silte do Solo a 30-60cm', 'geolyr': silteSolo, active: false},
]

var fixedLayers = [
    {'id': 1, 'title': 'América do Sul', 'geolyr': americaSul},
    {'id': 2, 'title': 'Oceano', 'geolyr': oceano},
]

const {createApp} = Vue

const app = createApp({
    data() {
        return {
            map: null,
            themeList: window.themeList,
            fixedLayers: window.fixedLayers,
            overlays: window.overlays,
            zoom: 8,
            bounds: window.bounds,
        }
    },
    methods: {
        initMap() {
            this.map = L.map('map', {
                    maxZoom: this.zoom,
                    zoomControl: false,
                    layers: [
                        this.themeList[0].geolyr, this.themeList[0].geolyr,
                        this.fixedLayers[0].geolyr,
                        this.fixedLayers[1].geolyr,
                        this.overlays[0].geolyr,
                    ]
                }
            ).fitBounds(this.bounds)
            var zoomHome = L.Control.zoomHome()
            zoomHome.addTo(this.map)
        },
        activeThemeLayer(id) {
            this.themeList.find(layer => {
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
            this.overlays.find(layer => {
                if (layer.id === id) {
                    layer.active = !layer.active
                    if (layer.active) {
                        this.map.addLayer(layer.geolyr)
                    } else {
                        this.map.removeLayer(layer.geolyr)
                    }
                }
            })
        },
    },
    mounted() {
        this.initMap()
    },
})

// Delimiters changed to ES6 template string style
app.config.compilerOptions.delimiters = ['${', '}']
app.mount('#app')
