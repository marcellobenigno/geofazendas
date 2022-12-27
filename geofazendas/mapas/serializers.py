from rest_framework import serializers

from .models import Estado, Municipio


class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = [
            'id',
            'nome',
            'sigla_uf',
            'area_km2',
        ]


class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = [
            'nome',
            'estado',
            'sigla_uf',
            'cod_ibge_m',
            'sede_lng',
            'sede_lat',
            'slug',
            'visivel',
        ]
