var themeList = [
    {
        id: 1,
        nome: 'Incidência Solar',
        slug: 'incidencia-solar',
        geolyr: incidencia,
        active: true,
        origem: 'incidencia',
        leg: getLegend('mapas_irradiacao'),
        referencia: '',
        link: '',
    },
];

var overlayList = overlayList.concat([

    {
        id: 9,
        nome: 'Subestação',
        slug: 'area_potencial',
        geolyr: subEstacao,
        active: false,
        origem: 'incidencia',
        leg: getLegend('mapas_subestacao'),
        referencia: '',
        link: '',
    },
    {
        id: 10,
        nome: 'Linhas de Transmissão',
        slug: 'area_potencial',
        geolyr: linhaTransmissao,
        active: false,
        origem: 'incidencia',
        leg: getLegend('mapas_linhatransmissao'),
        referencia: '',
        link: '',
    },
    {
        id: 11,
        nome: 'Área Potencial',
        slug: 'area_potencial',
        geolyr: areaPotencial,
        active: false,
        origem: 'incidencia',
        leg: getLegend('area_potencial'),
        referencia: '',
        link: '',
    }
])

