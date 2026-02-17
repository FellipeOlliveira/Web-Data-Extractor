
# GitHub Trending Scraper

Script em Python para extrair dados da página Trending do GitHub e gerar um arquivo CSV estruturado.

## 📌 Objetivo

Coletar automaticamente os repositórios em alta no GitHub e exportar no seguinte formato:

ranking;project;language;stars;stars_todays;forks

## 🚀 Tecnologias utilizadas

- Python 3
- requests
- BeautifulSoup4

## 📦 Instalação

Clone o repositório:

git clone https://github.com/FellipeOlliveira/Web-Data-Extractor.git

Entre na pasta:

cd Web-Data-Extractor

Instale as dependências:

pip install -r requirements.txt

## ▶️ Como executar

Execute o script:

python extraction.py

Após a execução será gerado o arquivo:

trending.csv

## 📊 Estrutura do CSV

| Campo | Descrição |
|-------|-----------|
| ranking | Posição no trending |
| project | Nome do repositório (owner/repo) |
| language | Linguagem principal |
| stars | Total de estrelas |
| stars_todays | Estrelas recebidas hoje |
| forks | Total de forks |

## 📁 Estrutura do projeto

.
├── main.py
├── trending.csv
├── requirements.txt
└── README.md

## 🔍 Fonte dos dados

Dados coletados da página pública:

https://github.com/trending

## ⚠️ Observação

O GitHub pode alterar a estrutura HTML da página, o que pode exigir atualização no parser.
