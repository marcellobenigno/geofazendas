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

wmsOptions['layers'] = 'geofazendas:mapas_car';
wmsOptions['zIndex'] = 1;

const car = L.tileLayer.wms(geoServerUrl, wmsOptions);

var bounds = JSON.parse($('#extent').val());


const map = L.map('map', {
    maxZoom: 22,
    layers: [googleStreets, car],
    zoomControl: false,
    maxBounds: bounds,
    minZoom: 5
});

map.fitBounds(bounds);

const baseLayers = {
    'Google Streets': googleStreets,
    'Google Satellite': googleSat,
    'Google Terrain': googleTerrain,
};


const overlays = {
    'Imóveis Rurais': car,
};

L.control.layers(baseLayers, overlays).addTo(map);


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