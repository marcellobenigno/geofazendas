$(document).ready(function () {
    $('#id_estado').select2({
        theme: 'bootstrap4',
        placeholder: "Escolha o Estado",
        "language": "pt-BR",
    });

    $('#id_estado').change(function () {
        let urlMunicipios = $('#search').data('urlmunicipios');
        let estadoID = $(this).val();
        $.ajax({
            url: urlMunicipios,
            data: {
                estado_id: estadoID
            },
            success: function (response) {
                $('#id_municipio').html(response);
                $("#id_municipio").select2().trigger('change');
            }
        })
    });

    $('#id_municipio').change(function () {
        let municipioExtent = $(this).val();

        if (municipioExtent) {
            map.fitBounds(JSON.parse(municipioExtent));
            municipio.addTo(map);
        }

    });
});