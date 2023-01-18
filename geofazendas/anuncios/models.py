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


class Anuncio(BaseModel):

    INFORMACOES_DIVULGAVEIS_CHOICES = [
        ('telefone-email', 'Telefone e E-mail'),
        ('telefone', 'Apenas Telefone'),
        ('email', 'Apenas E-mail'),
    ]
    TIPO_TRANSACAO_CHOICES = [
        ('venda', 'Venda'),
        ('troca', 'Troca'),
        ('arrendamentao', 'Arrendamentao'),
    ]

    proprietario = models.ForeignKey(
        'seguranca.Usuario', models.CASCADE, verbose_name='Proprietário', related_name='anuncios'
    )
    nome = models.CharField('Nome da Propriedade', max_length=50)
    matricula = models.CharField('Número da Matrícula do Imóvel', max_length=50)
    nome_responsavel = models.CharField('Nome do Responsável', max_length=50)
    email_responsavel = models.EmailField('E-mail do Responsável')
    telefone_contato = models.CharField('Telefone de Contato', max_length=20)
    informacoes_divulgaveis = models.CharField(
        'Informações Divulgavéis', max_length=20, choices=INFORMACOES_DIVULGAVEIS_CHOICES
    )
    descricao = models.TextField('Descrição da Propriedade', blank=True)
    area_ha = models.DecimalField('Área da Propriedade (ha)', decimal_places=2, max_digits=8)
    preco = models.DecimalField(
        'Preço de Comercialização', decimal_places=2, max_digits=10
    )
    divulga_preco = models.BooleanField('Divulgar Preço do Imóvel', default=False)
    municipio = models.ForeignKey('mapas.Municipio', models.CASCADE, verbose_name='Município')
    tipo_transacao = models.CharField('Tipo Transação', max_length=20, choices=TIPO_TRANSACAO_CHOICES)
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
