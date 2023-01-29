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
