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

var overlayList = [
    {
        id: 1,
        nome: 'Estados',
        geolyr: estado,
        active: true
    },
    {
        id: 2,
        nome: 'Municípios',
        geolyr: municipio,
        active: false
    },
    {
        id: 3,
        nome: 'Assentamentos',
        geolyr: assentamento,
        active: false
    },
    {
        id: 4,
        nome: 'Área Indígena',
        geolyr: areaIndigena,
        active: false
    },
    {
        id: 5,
        nome: 'Área Protegida',
        geolyr: areaProtegida,
        active: false
    },
    {
        id: 6,
        nome: 'Isoietas',
        geolyr: isoietas,
        active: false
    },
    {
        id: 7,
        nome: 'Imóveis a Venda',
        geolyr: imoveisVenda,
        active: false
    },
    {
        id: 8,
        nome: 'Área Potencial',
        slug: 'area_potencial',
        geolyr: areaPotencial,
        active: false,
        origem: 'incidencia',
        leg: getLegend('area_potencial'),
        referencia: '',
        link: '',
    },
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
        id: 8,
        nome: 'Área Potencial',
        slug: 'area_potencial',
        geolyr: areaPotencial,
        active: false,
        origem: 'incidencia',
        leg: getLegend('area_potencial'),
        referencia: '',
        link: '',
    },
]
