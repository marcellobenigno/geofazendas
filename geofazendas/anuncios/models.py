from django.db import models

from geofazendas.base.models import BaseModel


class Estrutura(BaseModel):

    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estrutura'
        verbose_name_plural = 'Estruturas'
        ordering = ['nome']


class OpcaoDiversos(BaseModel):

    CATEGORIA_CHOICES = [
        (v, v) for v in [
            'Alimentos',
            'Animais',
            'Defensivos Agrícolas',
            'Embalagens',
            'Exportação e Importação',
            'Fertilizantes Agrícolas',
            'Nutrição Animal',
            'Sementes',
            'Outros',
        ]
    ]

    categoria = models.CharField('Categoria', max_length=30)
    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Opção para Anúncio Diversos'
        verbose_name_plural = 'Opções para Anúncios Diversos'


class TipoServico(BaseModel):

    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tipo do Serviço'
        verbose_name_plural = 'Tipos de Serviços'


class Anuncio(BaseModel):

    UNIDADE_MEDIDA_CHOICES = [
        (v, v) for v in [
            'Hectare',
            'Alqueire',
            'Alqueire Mineiro/Alqueire Geométrico',
            'Alqueire Paulista',
            'Braça Quadrada',
            'Data',
            'Légua Quadrada',
            'Litro',
            'Metro Quadrado',
            'Mil Covas',
            'Quarta',
            'Tarefa',
            'Tarefa Baiana',
        ]
    ]
    TIPO_PROPRIEDADE_CHOICES = [
        (v, v) for v in [
            'Fazenda',
            'Chácara',
            'Sítio',
            'Rancho',
            'Outros',
        ]
    ]
    TIPO_BIOMA_CHOICES = [
        (v, v) for v in [
            'Amazônia',
            'Caatinga',
            'Cerrado',
            'Mata Atlântica',
            'Pampa',
            'Pantanal',
        ]
    ]
    TIPO_SERVICO_CHOICES = [
        (v, v) for v in [
            'Comércio/Corretoras/Representantes',
            'Compro/Procuro',
            'Consultoria Rural/Assessoria ',
            'Crédito Rural ',
            'Currículos',
            'Cursos/Palestras/Congressos/ Convenções',
            'Estágio',
            'Exportação/Importação ',
            'Feiras/Exposições/Leilões',
            'Fotos e Filmagens',
            'Fretes',
            'Georreferenciamento/Topografia',
            'Laboratórios',
            'Locação de Produtos',
            'Marcas e Patente',
            'Mecanização Agrícola',
            'Poços Artesianos/Semi-Artesianos',
            'Profissionais/Técnicos',
            'Seguro Rural',
            'TerceirizaçãTerraplenagem',
            'Tratamentos',
            'Turismo Rural',
            'Diversos',
        ]
    ]
    INFORMACOES_DIVULGAVEIS_CHOICES = [
        ('telefone-email', 'Telefone e E-mail'),
        ('telefone', 'Apenas Telefone'),
        ('email', 'Apenas E-mail'),
    ]
    TIPO_TRANSACAO_CHOICES = [
        ('venda', 'Venda'),
        ('troca', 'Troca'),
        ('arrendamento', 'Arrendamento'),
    ]
    TIPO_ANUNCIO_CHOICES = [
        ('propriedade', 'Propriedade'),
        ('reserva-legal', 'Reserva Legal'),
        ('energia-solar', 'Energia Solar'),
        ('equipamentos', 'Equipamentos'),
        ('servicos', 'Serviços'),
        ('diversos', 'Diversos'),
    ]

    proprietario = models.ForeignKey(
        'seguranca.Usuario', models.CASCADE, verbose_name='Proprietário', related_name='anuncios'
    )
    nome = models.CharField('Nome da Propriedade', max_length=50)
    matricula = models.CharField('Número da Matrícula do Imóvel', max_length=50, blank=True)
    tipo_anuncio = models.CharField(
        'Tipo do Anúncio', choices=TIPO_ANUNCIO_CHOICES, max_length=20, default='propriedade'
    )
    nome_responsavel = models.CharField('Nome do Responsável', max_length=50)
    email_responsavel = models.EmailField('E-mail do Responsável')
    telefone_contato = models.CharField('Telefone de Contato', max_length=20)
    informacoes_divulgaveis = models.CharField(
        'Informações Divulgavéis', max_length=20, choices=INFORMACOES_DIVULGAVEIS_CHOICES
    )
    descricao = models.TextField('Descrição da Propriedade', blank=True)
    unidade_medida = models.CharField(
        'Unidade de Medida', max_length=40, choices=UNIDADE_MEDIDA_CHOICES, blank=True
    )
    area_ha = models.DecimalField(
        'Área da Propriedade (ha)', decimal_places=2, max_digits=8, blank=True, null=True
    )
    preco = models.DecimalField(
        'Preço de Comercialização', decimal_places=2, max_digits=10, blank=True, null=True
    )
    destaque = models.BooleanField('Destaque', default=False)
    divulga_preco = models.BooleanField('Divulgar Preço do Imóvel', default=False)
    municipio = models.ForeignKey('mapas.Municipio', models.CASCADE, verbose_name='Município')
    tipo_transacao = models.CharField('Tipo Transação', max_length=20, choices=TIPO_TRANSACAO_CHOICES)
    tipo_servico = models.ForeignKey(
        TipoServico, models.SET_NULL, null=True, blank=True, verbose_name='Tipo do Serviço'
    )
    tipo_bioma = models.CharField('Tipo do Bioma', max_length=20, choices=TIPO_BIOMA_CHOICES, blank=True)
    tipo_propriedade = models.CharField(
        'Tipo da Propriedade', max_length=30, choices=TIPO_PROPRIEDADE_CHOICES, blank=True
    )
    opcao_diversos = models.ForeignKey(
        OpcaoDiversos, models.SET_NULL, blank=True, null=True, verbose_name='Opção Diversos'
    )
    foto = models.ImageField('Foto', upload_to='anuncios/fotos', null=True, blank=True)
    estruturas = models.ManyToManyField(Estrutura, blank=True, verbose_name='Estruturas na Propriedade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'


class ArquivoAnuncio(BaseModel):

    anuncio = models.ForeignKey(Anuncio, models.CASCADE, verbose_name='Anúncio', related_name='arquivos')
    arquivo = models.FileField('Arquivo', upload_to='anuncios/arquivos')

    def __str__(self):
        return self.arquivo.name.split('/')[-1]

    class Meta:
        verbose_name = 'Arquivo do Anúncio'
        verbose_name_plural = 'Arquivos dos Anúncios'
