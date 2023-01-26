var gstreets = L.tileLayer('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

var googleTerrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    attribution: 'google',
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

var clientsURL = 'https://sigctrm.com.br/prefeitura/api/clientes-multisig/';


function onEachFeature(feature, layer) {
    let out = `
        Anuncie o seu Imóvel Rural aqui!
    `;
    return layer.bindPopup(out);
}

var clients = L.geoJson(imoveisJson, {
    onEachFeature: onEachFeature,
    pointToLayer(feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 5,
            fillColor: '#ff7800',
            color: '#000',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });
    }
});

$.getJSON(clientsURL, function (data) {
    clients.addData(data);
});

var corner1 = L.latLng(5.397273407690917, -32.21191406250001);
var corner2 = L.latLng(-33.247875947924385, -78.00292968750001);
bounds = L.latLngBounds(corner1, corner2);

const map = L.map('map', {
    center: [-14.774882506516272, -54.25048828125001],
    zoom: 4,
    maxZoom: 22,
    layers: [googleTerrain, clients],
    zoomControl: false,
    minZoom: 5,
    maxBounds: bounds,
});

const zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);


var baseLayers = {
    "Google Maps": gstreets,
    "Google Terreno": googleTerrain,
};

var overlays = {
    "Imóveis a venda": clients,
};

L.control.layers(baseLayers, overlays).addTo(map);