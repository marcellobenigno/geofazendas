wmsOptions['zIndex'] = 1;
wmsOptions['layers'] = 'sigitr:maps_solo';

const solos = L.tileLayer.wms(geoServerUrl, wmsOptions).addTo(map);
layerControl.addOverlay(solos, "Solos");
