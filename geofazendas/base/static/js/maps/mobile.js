var bounds = JSON.parse($('#extent').val());
var id_municipio = $('#id_municipio').val();
var tematico = $('#tematico').val();
var municipio_nome = $('#municipio_nome').val();

console.log(themeList[tematico])

var municipio_selecionado = L.tileLayer.wms(geoServerUrl, {
    format: 'image/png',
    transparent: true,
    version: '1.1.0',
    maxZoom: 20,
    opacity: 1,
    zIndex: 5,
    layers: 'geofazendas:mapas_municipio_selecionado',
    cql_filter: `municipio_id=${id_municipio}`
});

const map = L.map('map', {
    maxZoom: 22,
    layers: [googleStreets],
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
    'Imóveis do CAR': car,
    'Municípios': municipio,
};

var layerControl = L.control.layers(baseLayers, overlays).addTo(map);

layerControl.addOverlay(municipio_selecionado, municipio_nome);


municipio.addTo(map);
municipio_selecionado.addTo(map);

if (tematico) {
    layerControl.addOverlay(themeList[tematico].geolyr, themeList[tematico].nome);
    municipio.bringToFront()
    municipio_selecionado.bringToFront()
    car.bringToFront()
}

