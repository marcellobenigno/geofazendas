const googleOpts = {
    maxZoom: 20,
    attribution: '&copy; <a href="https://www.google.com/">Google Maps</a>',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
};

const googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', googleOpts);
const googleSat = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', googleOpts);
const googleTerrain = L.tileLayer('https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', googleOpts);

var geoServerUrl = $('#geoserver_url').val();
geoServerUrl = geoServerUrl + 'geofazendas/wms?'

var wmsOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
};

wmsOptions['layers'] = 'geofazendas:america_sul';
wmsOptions['zIndex'] = 1;
const americaSul = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:oceano';
wmsOptions['zIndex'] = 1;
const oceano = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:ph_solo';
wmsOptions['zIndex'] = 2;
const phSolo = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:bioma';
wmsOptions['zIndex'] = 2;
const bioma = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:capaguadisp';
wmsOptions['zIndex'] = 2;
const capAguaDisp = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:clima';
wmsOptions['zIndex'] = 2;
const clima = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:declividade';
wmsOptions['zIndex'] = 2;
const declividade = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:geologia';
wmsOptions['zIndex'] = 2;
const geologia = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:geomorfologia';
wmsOptions['zIndex'] = 2;
const geomorfologia = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:condutividade_eletrica';
wmsOptions['zIndex'] = 2;
const CondutividadeEletrica = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:saturacao_sodio';
wmsOptions['zIndex'] = 2;
const saturacaoSodio = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:solo';
wmsOptions['zIndex'] = 2;
const solo = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:areia_disponivel_solo';
wmsOptions['zIndex'] = 2;
const areiaDisponivelSolo = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:argila_solo';
wmsOptions['zIndex'] = 2;
const argilaSolo = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:silte_solo';
wmsOptions['zIndex'] = 2;
const silteSolo = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_estadogeometria';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const estado = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_municipiogeometria';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const municipio = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_car';
const car = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_assentamento';
const assentamento = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_areaindigena';
const areaIndigena = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_areaprotegida';
const areaProtegida = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'geofazendas:mapas_isoieta';
const isoietas = L.tileLayer.wms(geoServerUrl, wmsOptions);
