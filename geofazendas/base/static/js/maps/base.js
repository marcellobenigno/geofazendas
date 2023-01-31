const googleOpts = {
    maxZoom: 20,
    attribution: '&copy; <a href="https://www.google.com/">Google Maps</a>',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
};
const googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', googleOpts);
const googleSat = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', googleOpts);
const googleTerrain = L.tileLayer('https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', googleOpts);


var sentinelURL = 'https://tiles.maps.eox.at/wms?';

var sentinelWmsOpts = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    zIndex: 3,
    attribution: '&copy; <a href="https://www.sentinel-hub.com/">Sentinel</a>'
};

sentinelWmsOpts['layers'] = 's2cloudless-2018_3857';
var s2cloudless_2017 = L.tileLayer.wms(sentinelURL, sentinelWmsOpts);

sentinelWmsOpts['layers'] = 's2cloudless-2018_3857';
var s2cloudless_2018 = L.tileLayer.wms(sentinelURL, sentinelWmsOpts);

sentinelWmsOpts['layers'] = 's2cloudless-2019_3857';
var s2cloudless_2019 = L.tileLayer.wms(sentinelURL, sentinelWmsOpts);

sentinelWmsOpts['layers'] = 's2cloudless-2020_3857';
var s2cloudless_2020 = L.tileLayer.wms(sentinelURL, sentinelWmsOpts);


var geoServerUrl = $('#geoserver_url').val();
geoServerUrl = geoServerUrl + 'geofazendas/wms?'

var ibgeWMSOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    attribution: '&copy; <a href="https://www.ibge.gov.br/">IBGE</a>',
};

ibgeWMSOptions['layers'] = 'geofazendas:america_sul';
ibgeWMSOptions['zIndex'] = 1
const americaSul = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:oceano';
ibgeWMSOptions['zIndex'] = 1
const oceano = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_bioma';
ibgeWMSOptions['zIndex'] = 2
const bioma = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_clima';
ibgeWMSOptions['zIndex'] = 2
const clima = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_declividade';
ibgeWMSOptions['zIndex'] = 2
const declividade = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_geologia';
ibgeWMSOptions['zIndex'] = 2
const geologia = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_geomorfologia';
ibgeWMSOptions['zIndex'] = 2
const geomorfologia = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

ibgeWMSOptions['layers'] = 'geofazendas:mapas_solo';
ibgeWMSOptions['zIndex'] = 2
const solo = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

// --------------------------------------------------------------------
var embrapaWmsptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    zIndex: 1,
    attribution: '&copy; <a href="http://geoinfo.cnps.embrapa.br/">EMBRAPA - GeoInfo</a>',
};

embrapaWmsptions['layers'] = 'geofazendas:mapas_argila_solo';
const argilaSolo = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);

embrapaWmsptions['layers'] = 'geofazendas:mapas_areia_disponivel_solo';
const areiaDisponivelSolo = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);

embrapaWmsptions['layers'] = 'geofazendas:mapas_ph_solo';
const phSolo = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);


embrapaWmsptions['layers'] = 'geofazendas:mapas_condutividade_eletrica';
const CondutividadeEletrica = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);

embrapaWmsptions['layers'] = 'geofazendas:mapas_saturacao_sodio';
const saturacaoSodio = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);

embrapaWmsptions['layers'] = 'geofazendas:mapas_silte_solo';
const silteSolo = L.tileLayer.wms(geoServerUrl, embrapaWmsptions);

var anaWmsptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    zIndex: 1,
    attribution: '&copy; <a href="https://dadosabertos.ana.gov.br/search">ANA</a>',
};


anaWmsptions['layers'] = 'geofazendas:mapas_capaguadisp';
const capAguaDisp = L.tileLayer.wms(geoServerUrl, anaWmsptions);

// -----------------------------------------------------------


var overlayWmsOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    zIndex: 10,
    opacity: 0.6,
    attribution: '&copy; <a href="https://www.ibge.gov.br/">IBGE</a>',
};

overlayWmsOptions['layers'] = 'geofazendas:mapas_estadogeometria';
const estado = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_municipiogeometria';
const municipio = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_car';
const car = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_assentamento';
const assentamento = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_areaindigena';
const areaIndigena = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_areaprotegida';
const areaProtegida = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_isoieta';
const isoietas = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);