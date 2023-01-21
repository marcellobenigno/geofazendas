var geoServerUrl = $('#geoserver_url').val();

geoServerUrl = geoServerUrl + 'geofazendas/wms?'

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

const googleOpts = {
    maxZoom: 20,
    attribution: '&copy; <a href="https://www.google.com/">Google Maps</a>',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
};

const googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', googleOpts);
const googleSat = L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', googleOpts);
const googleTerrain = L.tileLayer('https://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', googleOpts);

wmsOptions['layers'] = 'geofazendas:america_sul';
wmsOptions['zIndex'] = 1;
const americaSul = L.tileLayer.wms(geoServerUrl, wmsOptions);
americaSul.addTo(map);

wmsOptions['layers'] = 'geofazendas:oceano';
wmsOptions['zIndex'] = 1;
const oceano = L.tileLayer.wms(geoServerUrl, wmsOptions);
oceano.addTo(map)

wmsOptions['layers'] = `geofazendas:mapas_${themeName}`;
wmsOptions['zIndex'] = 100;
const theme = L.tileLayer.wms(geoServerUrl, wmsOptions);
theme.addTo(map)

const zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);

const baseLayers = {
    'Temático': theme,
};

const overlays = {};

const layerControl = L.control.layers(baseLayers, overlays).addTo(map);

layerControl.addBaseLayer(googleStreets, "Google Streets");
layerControl.addBaseLayer(googleSat, "Google Satélite");
layerControl.addBaseLayer(googleTerrain, "Google Terreno");

wmsOptions['layers'] = 'geofazendas:mapas_estadogeometria';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const estado = L.tileLayer.wms(geoServerUrl, wmsOptions);
estado.addTo(map);

wmsOptions['layers'] = 'geofazendas:mapas_municipiogeometria';
wmsOptions['zIndex'] = 10;
wmsOptions['opacity'] = 0.6;
const municipio = L.tileLayer.wms(geoServerUrl, wmsOptions);

layerControl.addOverlay(estado, "Estados");
layerControl.addOverlay(municipio, "Municípios");


var popup = L.popup();

function onMapClick(e) {
    map.spin(true, {lines: 20, length: 55});

    let url = $("#popup_url").val().slice(0, -12);

    url += `${e.latlng.lng}/${e.latlng.lat}/${themeName}/`;
    var request = $.ajax({
        url: url,
        method: "GET",
    });

    request.done(function (msg) {
        map.spin(false);
        if (msg.slugify()) {
            popup.setLatLng(e.latlng).setContent(msg).openOn(map);
        }
    });
}

map.on('click', onMapClick);