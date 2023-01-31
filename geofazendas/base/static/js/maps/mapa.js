var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2)

var overlayList = [
    {'id': 1, 'nome': 'Estados', 'geolyr': estado, active: true},
    {'id': 2, 'nome': 'Municípios', 'geolyr': municipio, active: false},
    {'id': 3, 'nome': 'Assentamentos', 'geolyr': assentamento, active: false},
    {'id': 4, 'nome': 'Área Indígena', 'geolyr': areaIndigena, active: false},
    {'id': 5, 'nome': 'Área Protegida', 'geolyr': areaProtegida, active: false},
    {'id': 6, 'nome': 'Isoietas', 'geolyr': isoietas, active: false},
]

var satteliteList = [
    {'id': 1, 'nome': 'Google Streets', 'geolyr': googleStreets, active: false},
    {'id': 2, 'nome': 'Google Sattelite', 'geolyr': googleSat, active: false},
    {'id': 3, 'nome': 'Google Terrain', 'geolyr': googleTerrain, active: false},
    {'id': 4, 'nome': 'Sentinel 2017', 'geolyr': s2cloudless_2017, active: false},
    {'id': 5, 'nome': 'Sentinel 2018', 'geolyr': s2cloudless_2018, active: false},
    {'id': 6, 'nome': 'Sentinel 2019', 'geolyr': s2cloudless_2019, active: false},
    {'id': 7, 'nome': 'Sentinel 2020', 'geolyr': s2cloudless_2020, active: false},
]


var themeList = [
    {'id': 1, 'nome': 'Biomas', 'geolyr': bioma, active: true, origem: 'ibge'},
    {'id': 2, 'nome': 'Clima', 'geolyr': clima, active: false, origem: 'ibge'},
    {'id': 3, 'nome': 'Declividade', 'geolyr': declividade, active: false, origem: 'ibge'},
    {'id': 4, 'nome': 'Geologia', 'geolyr': geologia, active: false, origem: 'ibge'},
    {'id': 5, 'nome': 'Geomorfologia', 'geolyr': geomorfologia, active: false, origem: 'ibge'},
    {'id': 6, 'nome': 'Solos', 'geolyr': solo, active: false, origem: 'ibge'},

    {'id': 7, 'nome': 'Teor de Argila do Solo a 30-60cm', 'geolyr': argilaSolo, active: false, origem: 'embrapa'},
    {'id': 8, 'nome': 'Teor de Areia do Solo a 30-60cm', 'geolyr': areiaDisponivelSolo, active: false, origem: 'embrapa'},
    {'id': 9, 'nome': 'Teor de Silte do Solo a 30-60cm', 'geolyr': silteSolo, active: false, origem: 'embrapa'},
    {'id': 10, 'nome': 'Condutividade Elétrica do Solo', 'geolyr': CondutividadeEletrica, active: false, origem: 'embrapa'},
    {'id': 11, 'nome': 'Saturação por Sódio do Solo a 30-100cm', 'geolyr': saturacaoSodio, active: false, origem: 'embrapa'},
    {'id': 12, 'nome': 'Acidez (pH) do Solo a 30-60cm', 'geolyr': phSolo, active: false, origem: 'embrapa'},
    {'id': 13, 'nome': 'Capacidade de Água Disponível (AWC)', 'geolyr': capAguaDisp, active: false, origem: 'ana'},
]

var fixedLayers = [
    {'id': 1, 'nome': 'América do Sul', 'geolyr': americaSul},
    {'id': 2, 'nome': 'Oceano', 'geolyr': oceano},
]

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
