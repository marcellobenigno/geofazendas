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
    opacity: 1,
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
    opacity: 1,
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

overlayWmsOptions['layers'] = 'geofazendas:mapas_imoveis_venda';
const imoveisVenda = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

function getLegend(lyrName) {
    let legend = `${geoServerUrl}REQUEST=GetLegendGraphic&`
    legend += 'VERSION=1.1.0&'
    legend += 'FORMAT=image/png&'
    legend += 'WIDTH=18&'
    legend += 'HEIGHT=18&'
    legend += `LAYER=geofazendas:${lyrName}&`
    legend += 'LEGEND_OPTIONS=fontName:Arial;fontAntiAliasing:true;dpi=200'
    return legend
}

var overlayList = [
    {
        id: 1,
        nome: 'Estados',
        geolyr: estado,
        active: true
    },
    {
        id: 2,
        nome: 'Municípios',
        geolyr: municipio,
        active: false
    },
    {
        id: 3,
        nome: 'Assentamentos',
        geolyr: assentamento,
        active: false
    },
    {
        id: 4,
        nome: 'Área Indígena',
        geolyr: areaIndigena,
        active: false
    },
    {
        id: 5,
        nome: 'Área Protegida',
        geolyr: areaProtegida,
        active: false
    },
    {
        id: 6,
        nome: 'Isoietas',
        geolyr: isoietas,
        active: false
    },
    {
        id: 7,
        nome: 'Imóveis a Venda',
        geolyr: imoveisVenda,
        active: false
    },
]

var satteliteList = [
    {
        id: 1,
        nome: 'Google Streets',
        geolyr: googleStreets,
        active: false
    },
    {
        id: 2,
        nome: 'Google Sattelite',
        geolyr: googleSat,
        active: false
    },
    {
        id: 3,
        nome: 'Google Terrain',
        geolyr: googleTerrain,
        active: false
    },
    {
        id: 4,
        nome: 'Sentinel 2017',
        geolyr: s2cloudless_2017,
        active: false
    },
    {
        id: 5,
        nome: 'Sentinel 2018',
        geolyr: s2cloudless_2018,
        active: false
    },
    {
        id: 6,
        nome: 'Sentinel 2019',
        geolyr: s2cloudless_2019,
        active: false
    },
    {
        id: 7,
        nome: 'Sentinel 2020',
        geolyr: s2cloudless_2020,
        active: false
    },
]

var themeList = [
    {
        id: 1,
        nome: 'Biomas',
        geolyr: bioma,
        active: true,
        origem: 'ibge',
        leg: getLegend('mapas_bioma'),
        referencia: 'IBGE - INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. Mapa de Biomas do Brasil. Rio de Janeiro: IBGE, 2003. Escala 1:5.000.000.',
        link: 'https://www.ibge.gov.br/geociencias/cartas-e-mapas/informacoes-ambientais/15842-biomas.html?=&t=acesso-ao-produto',

    },
    {
        id: 2,
        nome: 'Clima',
        geolyr: clima,
        active: false,
        origem: 'ibge',
        leg: getLegend('mapas_clima')
    },
    {
        id: 3,
        nome: 'Declividade',
        geolyr: declividade,
        active: false,
        origem: 'ibge',
        leg: getLegend('mapas_declividade')
    },
    {
        id: 4,
        nome: 'Geologia',
        geolyr: geologia,
        active: false,
        origem: 'ibge',
        leg: getLegend('mapas_geologia')
    },
    {
        id: 5,
        nome: 'Geomorfologia',
        geolyr: geomorfologia,
        active: false,
        origem: 'ibge',
        leg: getLegend('mapas_geomorfologia')
    },
    {
        id: 6,
        nome: 'Solos',
        geolyr: solo,
        active: false,
        origem: 'ibge',
        leg: getLegend('mapas_solo')
    },
    {
        id: 7,
        nome: 'Teor de Argila do Solo a 30-60cm',
        geolyr: argilaSolo,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_argila_solo')
    },
    {
        id: 8,
        nome: 'Teor de Areia do Solo a 30-60cm',
        geolyr: areiaDisponivelSolo,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_areia_disponivel_solo')
    },
    {
        id: 9,
        nome: 'Teor de Silte do Solo a 30-60cm',
        geolyr: silteSolo,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_silte_solo')
    },
    {
        id: 10,
        nome: 'Condutividade Elétrica do Solo',
        geolyr: CondutividadeEletrica,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_condutividade_eletrica')
    },
    {
        id: 11,
        nome: 'Saturação por Sódio do Solo a 30-100cm',
        geolyr: saturacaoSodio,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_saturacao_sodio')
    },
    {
        id: 12,
        nome: 'Acidez (pH) do Solo a 30-60cm',
        geolyr: phSolo,
        active: false,
        origem: 'embrapa',
        leg: getLegend('mapas_ph_solo')
    },
    {
        id: 13,
        nome: 'Capacidade de Água Disponível (AWC)',
        geolyr: capAguaDisp,
        active: false,
        origem: 'ana',
        leg: getLegend('mapas_capaguadisp')
    },
]

var fixedLayers = [
    {
        id: 1,
        nome: 'América do Sul',
        geolyr: americaSul
    },
    {
        id: 2,
        nome: 'Oceano',
        geolyr: oceano
    },
]