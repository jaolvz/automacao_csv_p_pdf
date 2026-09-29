import pandas as pd
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime

#criar pasta para os documentos
pasta_documentos = Path('documentos')
pasta_documentos.mkdir(exist_ok=True)

dados = pd.read_csv('funcionarios.csv')

data = datetime.now().strftime("%d/%m/%Y")

#carregar o template do pdf
env = Environment( 
    loader=FileSystemLoader('templates')
)

template= env.get_template('index.html')



with sync_playwright() as p:
    #abrir navegador somente uma vez para reutilizar
    browser = p.chromium.launch()
    page = browser.new_page()
     

    for _, funcionario in dados.iterrows():

        funcionario = funcionario.to_dict()
        funcionario["data"] = data

        html_renderizado = template.render(**funcionario)

        nome_arquivo = f"relatorio_{funcionario['nome'].replace(' ', '_')}.pdf"

        caminho_pdf = pasta_documentos / nome_arquivo

        page.set_content(
            html_renderizado,
            wait_until="networkidle"
        )

        page.pdf(
            path=caminho_pdf,
            format="A4",
            print_background=True,
            margin={
                "top": "2cm",
                "bottom": "2cm",
                "left": "2cm",
                "right": "2cm"
            }
        )

        print(f"PDF gerado: {caminho_pdf}")

    browser.close()
    #fechando o navegador

