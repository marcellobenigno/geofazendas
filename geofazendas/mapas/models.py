import json

from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Intersection
from django.contrib.gis.geos import Point


class Estado(models.Model):
    nome = models.CharField('nome', max_length=20)
    sigla_uf = models.CharField('abreviação', max_length=2)
    area_km2 = models.DecimalField(
        'área (km2)', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class EstadoGeometria(models.Model):
    estado = models.ForeignKey('Estado', verbose_name='estado', on_delete=models.PROTECT)
    cod_ibge_m = models.CharField('código IBGE', max_length=20)
    area_km2 = models.DecimalField('área (km2)', max_digits=10, decimal_places=2)
    geom = models.MultiPolygonField('geom', srid=4326)

    @property
    def get_extent(self):
        minlng, minlat, maxlng, maxlat = self.geom.extent
        return [[minlat, minlng], [maxlat, maxlng]]

    class Meta:
        ordering = ['cod_ibge_m']
        verbose_name = 'Geometria do Estado'
        verbose_name_plural = 'Geometrias dos Estados'


class Municipio(models.Model):
    nome = models.CharField('nome', max_length=40)
    estado = models.ForeignKey('Estado', verbose_name='estado', on_delete=models.PROTECT)
    sigla_uf = models.CharField('UF', max_length=2, blank=True, null=True)
    cod_ibge_m = models.CharField('código IBGE', max_length=20)
    sede_lng = models.FloatField('Longitude da Sede', blank=True, null=True)
    sede_lat = models.FloatField('Latitude da Sede', blank=True, null=True)
    slug = models.SlugField()
    visivel = models.BooleanField('visível?')

    def __str__(self):
        return '{}/{}'.format(self.nome, self.estado.sigla_uf, )

    @property
    def sede(self):
        return Point(self.sede_lng, self.sede_lat, srid=4326)

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ('sigla_uf', 'nome')


class MunicipioGeometria(models.Model):
    municipio = models.OneToOneField('Municipio', verbose_name='municipio', on_delete=models.PROTECT)
    retificado = models.BooleanField('Retificado', default=False)
    cod_ibge_m = models.CharField('código IBGE', max_length=20)
    area_km2 = models.DecimalField('Área (km2)', max_digits=10, decimal_places=2, blank=True, null=True)
    geom = models.MultiPolygonField('Geom', srid=4326)

    def __str__(self):
        return self.municipio.nome

    @property
    def extent(self):
        minlng, minlat, maxlng, maxlat = self.geom.extent
        return [[minlat, minlng], [maxlat, maxlng]]

    @property
    def vizinhos(self):
        qs = MunicipioGeometria.objects.filter(
            geom__intersects=self.geom).exclude(municipio=self.municipio)
        return [municipio.cod_ibge_m for municipio in qs if municipio.cod_ibge_m != self.cod_ibge_m]

    class Meta:
        verbose_name = 'Geometria do Município'
        verbose_name_plural = 'Geometrias dos Municípios'
        ordering = ('cod_ibge_m',)


class Fuso(models.Model):
    fuso = models.IntegerField('fuso')
    codigo = models.IntegerField('Código EPSG', null=True, blank=True)
    geom = models.MultiPolygonField('geom', srid=4326)

    def __str__(self):
        return f'fuso: {self.fuso}'

    class Meta:
        verbose_name = 'Fuso'
        verbose_name_plural = 'Fusos'


class IncraSigef(models.Model):
    parcela_co = models.CharField(
        'parcela', max_length=64, null=True, blank=True)
    rt = models.CharField('rt', max_length=10, null=True, blank=True)
    art = models.CharField('art', max_length=100, null=True, blank=True)
    situacao_i = models.CharField(
        'situação', max_length=25, null=True, blank=True)
    codigo_imo = models.CharField(
        'código do imóvel', db_index=True, max_length=13, null=True, blank=True)
    data_submi = models.DateField('data de submissão', null=True, blank=True)
    data_aprov = models.DateField('data de aprovação', null=True, blank=True)
    status = models.CharField('status', max_length=32, null=True, blank=True)
    nome_area = models.CharField(
        'nome da área', max_length=254, null=True, blank=True)
    registro_m = models.CharField(
        'registro m', max_length=254, null=True, blank=True)
    registro_d = models.DateField('registro d', null=True, blank=True)
    municipio = models.IntegerField('município', null=True, blank=True)
    uf_id = models.IntegerField('uf id', null=True, blank=True)
    geom = models.MultiPolygonField('geom', srid=4326, null=True, blank=True)

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo_imo}"

    @property
    def get_centroid(self):
        return {'y': self.geom.centroid.y, 'x': self.geom.centroid.x}

    @property
    def get_json_geom(self):
        return json.loads(self.geom.json)

    @property
    def model_name(self):
        return 'IncraSigef'

    def area_calc(self):
        fusos = Fuso.objects.filter(geom__intersects=self.geom.buffer(0)).annotate(
            intersection_geom=Intersection('geom', self.geom.buffer(0))
        )
        fusos_list = [{'fuso': fuso.codigo, 'area': fuso.intersection_geom.area} for fuso in fusos]
        fuso = max(fusos_list, key=lambda x: x['area'])

        self.geom.transform(fuso['fuso'])

        return self.geom.area / 10000

    class Meta:
        verbose_name = 'Propriedade do INCRA - SIGEF'
        verbose_name_plural = 'Propriedades do INCRA - SIGEF'


class IncraSnci(models.Model):
    num_proces = models.CharField(
        'número do processo', max_length=70, null=True, blank=True)
    sr = models.CharField('sr', max_length=10, null=True, blank=True)
    num_certif = models.CharField(
        'número do cetificado', max_length=20, null=True, blank=True)
    data_certi = models.DateField(
        'data de certificação', null=True, blank=True)
    qtd_area_p = models.CharField(
        'quaantidade de área p', max_length=50, null=True, blank=True)
    cod_profis = models.CharField(
        'cód profissional', max_length=30, null=True, blank=True)
    cod_imovel = models.CharField(
        'código do imóvel', db_index=True, max_length=30, null=True, blank=True)
    nome_imove = models.CharField(
        'número do imóvel', max_length=255, null=True, blank=True)
    uf_municip = models.CharField('uf', max_length=2, null=True, blank=True)
    municipio = models.IntegerField('município', null=True, blank=True)
    geom = models.MultiPolygonField('geom', srid=4326, null=True, blank=True)

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.cod_imovel

    @property
    def get_centroid(self):
        return {'y': self.geom.centroid.y, 'x': self.geom.centroid.x}

    @property
    def get_json_geom(self):
        return json.loads(self.geom.json)

    @property
    def model_name(self):
        return 'incraSnci'

    class Meta:
        verbose_name = 'Propriedade do INCRA - SNCI'
        verbose_name_plural = 'Propriedades do INCRA - SNCI'


class Car(models.Model):
    cod_imovel = models.CharField(max_length=100, null=True, blank=True)
    num_area = models.FloatField()
    cod_estado = models.CharField(max_length=2, null=True, blank=True)
    nom_munici = models.CharField(max_length=80, null=True, blank=True)
    num_modulo = models.FloatField()
    tipo_imove = models.CharField(max_length=10, null=True, blank=True)
    situacao = models.CharField(max_length=10, null=True, blank=True)
    condicao_i = models.CharField(max_length=100, null=True, blank=True)
    cod_ibge_m = models.CharField(max_length=20, null=True, blank=True)
    cod_ibge_e = models.CharField(max_length=20, null=True, blank=True)
    anunciado = models.BooleanField('anunciado?', default=False, null=True)
    geom = models.MultiPolygonField(srid=4326)

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.cod_imovel

    def area_calc(self):
        fusos = Fuso.objects.filter(geom__intersects=self.geom.buffer(0)).annotate(
            intersection_geom=Intersection('geom', self.geom.buffer(0))
        )
        fusos_list = [{'fuso': fuso.codigo, 'area': fuso.intersection_geom.area} for fuso in fusos]
        fuso = max(fusos_list, key=lambda x: x['area'])

        self.geom.transform(fuso['fuso'])

        return self.geom.area / 10000

    @property
    def model_name(self):
        return 'Car'

    class Meta:
        verbose_name = 'Imóvel do CAR'
        verbose_name_plural = 'Imóveis do CAR'


class AreaIndigena(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    geometriaa = models.CharField(max_length=254, blank=True, null=True)
    codidentif = models.CharField(max_length=80, blank=True, null=True)
    arealegal = models.FloatField(blank=True, null=True)
    classifica = models.CharField(max_length=80, blank=True, null=True)
    administra = models.CharField(max_length=254, blank=True, null=True)
    jurisdicao = models.CharField(max_length=254, blank=True, null=True)
    situacaoju = models.CharField(max_length=254, blank=True, null=True)
    datasituac = models.CharField(max_length=80, blank=True, null=True)
    grupoetnic = models.CharField(max_length=150, blank=True, null=True)
    perimetroo = models.FloatField(blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    cod_ibge_m = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Área Indígena'
        verbose_name_plural = 'Áreas Indígenas'


class AreaProtegida(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)
    geometriaa = models.CharField(max_length=254, blank=True, null=True)
    codidentif = models.CharField(max_length=80, blank=True, null=True)
    arealegal = models.FloatField(blank=True, null=True)
    anocriacao = models.CharField(max_length=4, blank=True, null=True)
    historicom = models.CharField(max_length=254, blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    areaoficia = models.CharField(max_length=16, blank=True, null=True)
    administra = models.CharField(max_length=254, blank=True, null=True)
    classifica = models.CharField(max_length=100, blank=True, null=True)
    jurisdicao = models.CharField(max_length=254, blank=True, null=True)
    tipounidpr = models.CharField(max_length=254, blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    cod_ibge_m = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Área Protegida'
        verbose_name_plural = 'Áreas Protegidas'


class Assentamento(models.Model):
    cd_sipra = models.CharField(max_length=254, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    nome_proje = models.CharField(max_length=254, blank=True, null=True)
    municipio = models.CharField(max_length=254, blank=True, null=True)
    area_hecta = models.CharField(max_length=40, blank=True, null=True)
    capacidade = models.BigIntegerField(blank=True, null=True)
    num_famili = models.BigIntegerField(blank=True, null=True)
    fase = models.BigIntegerField(blank=True, null=True)
    data_de_cr = models.CharField(max_length=10, blank=True, null=True)
    forma_obte = models.CharField(max_length=50, blank=True, null=True)
    data_obten = models.CharField(max_length=10, blank=True, null=True)
    area_calc = models.FloatField(blank=True, null=True)
    sr = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    cod_ibge_m = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.nome_proje}'

    class Meta:
        verbose_name = 'Assentamento'
        verbose_name_plural = 'Assentamentos'


class Bioma(models.Model):
    descricao = models.CharField(
        'descrição', max_length=50, blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Bioma: {}".format(self.descricao)

    class Meta:
        verbose_name = 'bioma'
        verbose_name_plural = 'biomas'


class Clima(models.Model):
    descricao = models.CharField(
        'descrição', max_length=120, blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Clima: {}".format(self.descricao)

    class Meta:
        verbose_name = 'clima'
        verbose_name_plural = 'climas'


class Declividade(models.Model):
    descricao = models.CharField(
        'descrição', max_length=250, blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Declividade: {}".format(self.descricao)

    class Meta:
        verbose_name = 'declividade'
        verbose_name_plural = 'declividades'


class Geologia(models.Model):
    descricao = models.CharField(
        'descrição', max_length=250, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Geologia: {}".format(self.descricao)

    class Meta:
        verbose_name = 'geologia'
        verbose_name_plural = 'geologia'


class Geomorfologia(models.Model):
    descricao = models.CharField(
        'descrição', max_length=70, blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Geomorfologia: {}".format(self.descricao)

    class Meta:
        verbose_name = 'geomorfologia'
        verbose_name_plural = 'geomorfologia'


class Isoieta(models.Model):
    descricao = models.IntegerField('descrição', blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiLineStringField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Isoieta: {}".format(self.descricao)

    class Meta:
        verbose_name = 'isoieta'
        verbose_name_plural = 'isoietas'


class Relevo(models.Model):
    descricao = models.CharField(
        'descrição', max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Relevo: {}".format(self.descricao)

    class Meta:
        verbose_name = 'relevo'
        verbose_name_plural = 'relevo'


class Solo(models.Model):
    descricao = models.CharField(
        'descrição', max_length=60, blank=True, null=True)
    cod_ibge_m = models.CharField(
        'código IBGE', max_length=8, blank=True, null=True)
    geom = models.MultiPolygonField('geom')

    criado = models.DateTimeField('Criado', auto_now_add=True, blank=True, null=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Solo: {}".format(self.descricao)

    class Meta:
        verbose_name = 'solo'
        verbose_name_plural = 'solos'


class LinhaTransmissao(models.Model):
    nome = models.CharField(max_length=70, blank=True, null=True)
    tensao_kv = models.BigIntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=16, blank=True, null=True)
    tipo_rede = models.CharField(max_length=18, blank=True, null=True)
    agente = models.CharField(max_length=19, blank=True, null=True)
    km = models.FloatField(blank=True, null=True)
    dt_ent_op = models.CharField(max_length=11, blank=True, null=True)
    dt_prev_op = models.CharField(max_length=13, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4326)


class Subestacao(models.Model):
    nome = models.CharField(max_length=35, blank=True, null=True)
    situacao = models.CharField(max_length=14, blank=True, null=True)
    municipio = models.CharField(max_length=35, blank=True, null=True)
    uf = models.CharField(max_length=4, blank=True, null=True)
    munic_uf = models.CharField(max_length=40, blank=True, null=True)
    geocodigo = models.BigIntegerField(blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    nome3 = models.CharField(max_length=250, blank=True, null=True)
    geom = models.PointField(srid=4326)


class Irradiacao(models.Model):
    country = models.CharField(max_length=6, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    annual = models.IntegerField(blank=True, null=True)
    jan = models.IntegerField(blank=True, null=True)
    feb = models.IntegerField(blank=True, null=True)
    mar = models.IntegerField(blank=True, null=True)
    apr = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    jun = models.IntegerField(blank=True, null=True)
    jul = models.IntegerField(blank=True, null=True)
    aug = models.IntegerField(blank=True, null=True)
    sep = models.IntegerField(blank=True, null=True)
    oct = models.IntegerField(blank=True, null=True)
    nov = models.IntegerField(blank=True, null=True)
    dec = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
