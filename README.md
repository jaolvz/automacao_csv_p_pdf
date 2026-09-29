# Automação CSV para PDF

Script em Python que lê dados de funcionários de um arquivo CSV e gera automaticamente relatórios de pagamento em PDF.

## Tecnologias

* Python
* Pandas
* Jinja2
* Playwright
* HTML/CSS

## Como usar

Instale as dependências:

pip install -r requirements.txt

Instale o Chromium do Playwright:

playwright install chromium

Execute:

python main.py

Os PDFs serão gerados na pasta `documentos/`.

## Estrutura

* main.py
* funcionarios.csv
* requirements.txt
* templates/index.html
* documentos/

Os dados utilizados no projeto são fictícios.
