# Geofazendas Back-End

## Requisitos
* Python 3.8.0
* PostgreSQL >= 10
* PostGIS >=2.5.1
* GDAL, no linux instale com: `apt-get install python-gdal`. Se for mac um `brew install gdal` é suficiente.

## Configurações do Banco de Dados Espaciais

É necessário criar um banco **PostgreSQL** e habilitar a extensão espacial **PostGIS**, no terminal, faça:

```
createdb geofazendas
psql geofazendas
CREATE EXTENSION postgis;
\d
```

## Como desenvolver?

* Clone o repositório;
* Crie um virtualenv com Python 3.8.0;
* Ative o virtualenv;
* Instale as dependências do ambiente de desenvolvimento;
* Crie o banco de dados espacial como foi descrito acima.


```
git clone https://github.com/marcellobenigno/geofazendas-backend.git
cd geofazendas-backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


* Preencha as informações do `.env` e rode os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
```

## Carga de Dados Espaciais:

Baixe o arquivo compactado do link: https://drive.google.com/file/d/1goPjAb9wG_U0-q8ZaFO1fWcvjqsfsopy/view?usp=sharing

Utilize o ```psql -f nome-do-arquivo.sql -d geofazendas``` na sequência dos nomes dos arquivos.


- Destaques: Notícias em destaques
