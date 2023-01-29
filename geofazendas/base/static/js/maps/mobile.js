var bounds = JSON.parse($('#extent').val());

const map = L.map('map', {
    maxZoom: 22,
    layers: [googleStreets, car],
    zoomControl: false,
    maxBounds: bounds,
    minZoom: 5
});
map.fitBounds(bounds);

const zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);


const baseLayers = {
    'Google Streets': googleStreets,
    'Google Satellite': googleSat,
    'Google Terrain': googleTerrain,
};

const overlays = {
    'Imóveis Rurais': car,
};

L.control.layers(baseLayers, overlays).addTo(map);
