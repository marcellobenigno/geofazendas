var geoServerUrl = $('#geoserver_url').val();

console.log(themeName);

geoServerUrl = geoServerUrl + 'sigitr/wms?'

var wmsOptions = {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
};

var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2);

const map = L.map('map', {
    maxZoom: 22,
    layers: [],
    zoomControl: false,
    maxBounds: bounds,
    minZoom: 5
});

map.fitBounds(bounds);

wmsOptions['layers'] = 'sigitr:america_sul';
wmsOptions['zIndex'] = 1;
const americaSul = L.tileLayer.wms(geoServerUrl, wmsOptions);
americaSul.addTo(map);

wmsOptions['layers'] = 'sigitr:oceano';
wmsOptions['zIndex'] = 1;
const oceano = L.tileLayer.wms(geoServerUrl, wmsOptions);
oceano.addTo(map)

wmsOptions['layers'] = `sigitr:maps_${themeName}`;
wmsOptions['zIndex'] = 100;
const theme = L.tileLayer.wms(geoServerUrl, wmsOptions);
theme.addTo(map)

const zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);

const baseLayers = {
    'Biomas': theme,
};

const overlays = {};

const layerControl = L.control.layers(baseLayers, overlays).addTo(map);


wmsOptions['layers'] = 'sigitr:maps_estado';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const estado = L.tileLayer.wms(geoServerUrl, wmsOptions);
estado.addTo(map);

wmsOptions['layers'] = 'sigitr:maps_geometriamunicipio';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const municipio = L.tileLayer.wms(geoServerUrl, wmsOptions);

layerControl.addOverlay(estado, "Estados");
layerControl.addOverlay(municipio, "Municípios");
