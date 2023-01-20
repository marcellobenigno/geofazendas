if (themeName === 'irradiacao') {
    wmsOptions['layers'] = 'geofazendas:mapas_linhatransmissao';
    wmsOptions['zIndex'] = 12;
    wmsOptions['opacity'] = 1;
    const linhaTransmissao = L.tileLayer.wms(geoServerUrl, wmsOptions);
    layerControl.addOverlay(linhaTransmissao, "Linhas de Transmissão");
    linhaTransmissao.addTo(map);

    wmsOptions['layers'] = 'geofazendas:area_potencial';
    wmsOptions['zIndex'] = 12;
    wmsOptions['opacity'] = 1;
    const areaPotencial = L.tileLayer.wms(geoServerUrl, wmsOptions);
    layerControl.addOverlay(areaPotencial, "Área Potencial");
    areaPotencial.addTo(map);

    wmsOptions['layers'] = 'geofazendas:mapas_subestacao';
    wmsOptions['zIndex'] = 12;
    wmsOptions['opacity'] = 1;
    const subestacao = L.tileLayer.wms(geoServerUrl, wmsOptions);
    layerControl.addOverlay(subestacao, "Subestação");
    subestacao.addTo(map);
}