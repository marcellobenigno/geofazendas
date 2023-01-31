var geoServerUrl = $('#geoserver_url').val() + 'geofazendas/wms?'


var googleOpts = {
    maxZoom: 22,
    minZoom: 5,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
}
var googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', googleOpts)
var googleSatellite = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', googleOpts)

var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2)

var wmsOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
}

wmsOptions['layers'] = 'geofazendas:america_sul'
wmsOptions['zIndex'] = 1
const americaSul = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:oceano'
wmsOptions['zIndex'] = 1
const oceano = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_ph_solo'
wmsOptions['zIndex'] = 2
const phSolo = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_bioma'
wmsOptions['zIndex'] = 2
const bioma = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_capaguadisp'
wmsOptions['zIndex'] = 2
const capAguaDisp = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_clima'
wmsOptions['zIndex'] = 2
const clima = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_declividade'
wmsOptions['zIndex'] = 2
const declividade = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_geologia'
wmsOptions['zIndex'] = 2
const geologia = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_geomorfologia'
wmsOptions['zIndex'] = 2
const geomorfologia = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_condutividade_eletrica'
wmsOptions['zIndex'] = 2
const CondutividadeEletrica = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_saturacao_sodio'
wmsOptions['zIndex'] = 2
const saturacaoSodio = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_solo'
wmsOptions['zIndex'] = 2
const solo = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_areia_disponivel_solo'
wmsOptions['zIndex'] = 2
const areiaDisponivelSolo = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_argila_solo'
wmsOptions['zIndex'] = 2
const argilaSolo = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_silte_solo'
wmsOptions['zIndex'] = 2
const silteSolo = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_estadogeometria'
wmsOptions['zIndex'] = 10
wmsOptions['opacity'] = 0.6
const estado = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_municipiogeometria'
wmsOptions['zIndex'] = 10
wmsOptions['opacity'] = 0.6
const municipio = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_car'
const car = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_assentamento'
const assentamento = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_areaindigena'
const areaIndigena = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_areaprotegida'
const areaProtegida = L.tileLayer.wms(geoServerUrl, wmsOptions)

wmsOptions['layers'] = 'geofazendas:mapas_isoieta'
const isoietas = L.tileLayer.wms(geoServerUrl, wmsOptions)

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
            googleOpts: {
                maxZoom: 20,
                minZoom: 9,
                subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
            },
            baseLayers: [
                {
                    id: 'googleStreets',
                    description: 'Google Streets',
                    lyr: window.googleStreets,
                    active: true
                },
                {
                    id: 'googleSatellite',
                    description: 'Google Satélite',
                    lyr: window.googleSatellite,
                    active: false
                }
            ],
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
