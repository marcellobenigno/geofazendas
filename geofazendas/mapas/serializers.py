from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Estado, Municipio, Car


class CarSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Car
        geo_field = 'geom'

        fields = [
            'id',
            'cod_imovel',
            'num_area',
            'cod_estado',
            'num_modulo',
            'tipo_imove',
            'situacao',
            'condicao_i',
            'cod_ibge_m',
            'cod_ibge_e',
            'anunciado',
            'geom',
        ]


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
            'id',
            'nome',
            'estado',
            'sigla_uf',
            'cod_ibge_m',
            'slug',
            'visivel',
            'extent',
        ]
