var geoServerUrl = $('#geoserver_url').val();

const googleOpts = {
    maxZoom: 20,
    attribution: '&copy; <a href="https://www.google.com/">Google Maps</a>',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
};

const googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', googleOpts);

const googleSat = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', googleOpts);

const googleTerrain = L.tileLayer('https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', googleOpts);


const map = L.map('map', {
    center: [-15.70775407, -53.5253906],
    zoom: 4,
    maxZoom: 22,
    layers: [googleStreets,],

});

const baseLayers = {
    'Google Streets': googleStreets,
    'Google Satellite': googleSat,
    'Google Terrain': googleTerrain,
};

const overlays = {};

const layerControl = L.control.layers(baseLayers, overlays).addTo(map);

geoServerUrl = geoServerUrl + 'sigitr/wms?'

const wmsOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
};

wmsOptions['layers'] = 'sigitr:maps_car';
wmsOptions['zIndex'] = 10;
const car = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'sigitr:maps_incrasigef';
wmsOptions['zIndex'] = 10;
const sigef = L.tileLayer.wms(geoServerUrl, wmsOptions);

wmsOptions['layers'] = 'sigitr:maps_incrasnci';
wmsOptions['zIndex'] = 10;
const snci = L.tileLayer.wms(geoServerUrl, wmsOptions);

layerControl.addOverlay(car, "CAR");
layerControl.addOverlay(sigef, "INCRA - SIGEF");
layerControl.addOverlay(snci, "INCRA - SNCI");


car.addTo(map);