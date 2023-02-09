if (!String.prototype.slugify) {
    String.prototype.slugify = function () {

        return this.toString().toLowerCase()
            .replace(/[àÀáÁâÂãäÄÅåª]+/g, 'a')       // Special Characters #1
            .replace(/[èÈéÉêÊëË]+/g, 'e')        // Special Characters #2
            .replace(/[ìÌíÍîÎïÏ]+/g, 'i')        // Special Characters #3
            .replace(/[òÒóÓôÔõÕöÖº]+/g, 'o')        // Special Characters #4
            .replace(/[ùÙúÚûÛüÜ]+/g, 'u')        // Special Characters #5
            .replace(/[ýÝÿŸ]+/g, 'y')            // Special Characters #6
            .replace(/[ñÑ]+/g, 'n')                // Special Characters #7
            .replace(/[çÇ]+/g, 'c')                // Special Characters #8
            .replace(/[ß]+/g, 'ss')                // Special Characters #9
            .replace(/[Ææ]+/g, 'ae')                // Special Characters #10
            .replace(/[Øøœ]+/g, 'oe')            // Special Characters #11
            .replace(/[%]+/g, 'pct')                // Special Characters #12
            .replace(/\s+/g, '-')                // Replace spaces with -
            .replace(/[^\w\-]+/g, '')            // Remove all non-word chars
            .replace(/\-\-+/g, '-')                // Replace multiple - with single -
            .replace(/^-+/, '')                    // Trim - from start of text
            .replace(/-+$/, '');            		// Trim - from end of text

    };
}

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

var estadosURL = $('#estados-api').val();
var municipiosURL = $('#municipios-api').val();

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


ibgeWMSOptions['layers'] = 'geofazendas:mapas_irradiacao';
ibgeWMSOptions['zIndex'] = 2
const incidencia = L.tileLayer.wms(geoServerUrl, ibgeWMSOptions);

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
// ------------------------------------------------------------------------
var mapBiomasWmsptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    zIndex: 1,
    attribution: '&copy; <a href="https://mapbiomas.org/">MapBiomas</a>',
};


mapBiomasWmsptions['layers'] = 'geofazendas:mapbiomas_2021';
const mapBiomas2021 = L.tileLayer.wms(geoServerUrl, mapBiomasWmsptions);

// -----------------------------------------------------------

function minTwoDigits(n) {
    return (n < 10 ? '0' : '') + n;
}

var dataConsulta = $('#data_atual').val().split('/')
var dia = parseInt(dataConsulta[0]) - 1
var mes = minTwoDigits(parseInt(dataConsulta[1]));
var ano = `${dataConsulta[2]}`;
dia = minTwoDigits(dia);

var ndscWMSOptions = {
    format: 'image/png',
    layers: 'observacao_ndsc_obs',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    opacity: 1,
    ANO: ano,
    MES: mes,
    DIA: dia,
    tiled: true,
    zIndex: 2,
    attribution: '&copy; <a href="https://queimadas.dgi.inpe.br/queimadas/portal/risco-de-fogo-meteorologia">INPE</a>'
};

const inpeURLndsc = 'https://sirc.dgi.inpe.br/cgi-bin/mapserv?map=/dados/mapfiles/riscofogo.map&';

const ndsc = L.tileLayer.wms(inpeURLndsc, ndscWMSOptions);

var inpeWMSOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.3',
    maxZoom: 20,
    opacity: 1,
    tiled: true,
    zIndex: 3,
    request: 'GetMap',
    service: 'WMS',
    attribution: '&copy; <a href="https://queimadas.dgi.inpe.br/queimadas/portal/risco-de-fogo-meteorologia">INPE</a>'
};

inpeURL = 'https://queimadas.dgi.inpe.br/queimadas/firerisk/geoserver/wms';

inpeWMSOptions['layers'] = 'inpe:Precipitation-Forecast_T0';
const precip0 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:Precipitation-Forecast_T1';
const precip1 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:Precipitation-Forecast_T2';
const precip2 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:Precipitation-Forecast_T3';
const precip3 = L.tileLayer.wms(inpeURL, inpeWMSOptions);


inpeWMSOptions['layers'] = 'inpe:RelativeHumidity-Forecast_T0';
const umidade0 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:RelativeHumidity-Forecast_T1';
const umidade1 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:RelativeHumidity-Forecast_T2';
const umidade2 = L.tileLayer.wms(inpeURL, inpeWMSOptions);
inpeWMSOptions['layers'] = 'inpe:RelativeHumidity-Forecast_T3';
const umidade3 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:Temperature-Forecast_T0';
const temperatura0 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:Temperature-Forecast_T1';
const temperatura1 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:Temperature-Forecast_T2';
const temperatura2 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:Temperature-Forecast_T3';
const temperatura3 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:FireRisk-Forecast_T0';
const riscoFogo0 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:FireRisk-Forecast_T1';
const riscoFogo1 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:FireRisk-Forecast_T2';
const riscoFogo2 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

inpeWMSOptions['layers'] = 'inpe:FireRisk-Forecast_T3';
const riscoFogo3 = L.tileLayer.wms(inpeURL, inpeWMSOptions);

// ---------------------------------------------------------
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

overlayWmsOptions['layers'] = 'geofazendas:area_potencial';
const areaPotencial = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_subestacao';
const subEstacao = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

overlayWmsOptions['layers'] = 'geofazendas:mapas_linhatransmissao';
const linhaTransmissao = L.tileLayer.wms(geoServerUrl, overlayWmsOptions);

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

var queimadasURL = $('#queimadas_url').val();

var focoStyle = {
    radius: 3,
    fillColor: 'yellow',
    color: 'red',
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

var foco48HsParameters = {
    service: 'WFS',
    version: '1.0.0',
    request: 'getFeature',
    typeName: 'queimadas:focos_brasil_48h',
    maxFeatures: 5000,
    outputFormat: 'application/json',
    type: 'geojson',
    format: 'geojson',
    srsName: 'EPSG:4326',
};

function onEachFeature(feature, layer) {
    let out = `
        <b>Município:</b> ${feature.properties.municipio || '-'}<br>
        <b>Precipitação:</b> ${feature.properties.precipitacao || '-'} mm<br>
        <b>Núm de dias sem chuva:</b> ${feature.properties.numero_dias_sem_chuva || '-'}<br>
        <b>Risco de Fogo:</b> ${feature.properties.risco_fogo || '-'}<br>
        <b>Bioma:</b> ${feature.properties.bioma || '-'}<br>
    `;
    return layer.bindPopup(out);
}

var focos48Hs = L.geoJson([], {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, focoStyle);
    },
    onEachFeature: onEachFeature,
});

$.getJSON(queimadasURL + L.Util.getParamString(foco48HsParameters), function (data) {
    focos48Hs.addData(data);
});

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
    {
        id: 8,
        nome: 'Focos de Incêndio das Últimas 48hs',
        slug: 'foco-incendio',
        geolyr: focos48Hs,
        active: false,
        origem: 'foco48hs',
        referencia: '',
        link: '',
    }
]



