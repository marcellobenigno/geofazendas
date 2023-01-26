var corner1 = L.latLng(-33.7511779940000025, -73.9831821599999984),
    corner2 = L.latLng(5.2695808330000000, -28.8477703530000014),
    bounds = L.latLngBounds(corner1, corner2);

const popup = L.popup();

const map = L.map('map', {
    maxZoom: 22,
    layers: [],
    zoomControl: false,
    maxBounds: bounds,
    minZoom: 5
});

map.fitBounds(bounds);

americaSul.addTo(map);
oceano.addTo(map)
estado.addTo(map);

wmsOptions['layers'] = `geofazendas:mapas_${themeName}`;
wmsOptions['zIndex'] = 100;
wmsOptions['opacity'] = 1;
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

layerControl.addOverlay(estado, "Estados");
layerControl.addOverlay(municipio, "Municípios");

layerControl.addOverlay(assentamento, "Assentamentos");
layerControl.addOverlay(areaIndigena, "Área Indígena");
layerControl.addOverlay(areaProtegida, "Área Protegida");
layerControl.addOverlay(isoietas, "Isoietas");

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