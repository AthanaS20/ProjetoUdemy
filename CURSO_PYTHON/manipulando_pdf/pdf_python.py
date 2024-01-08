# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
CAMINHO_PDF_ORIGINAL = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = CAMINHO_PDF_ORIGINAL / 'R20221007.pdf'

PASTA_NOVA.mkdir(exist_ok=True)
reader = PdfReader(RELATORIO_BACEN)

page_1 = reader.pages[0]
imagem_1 = page_1.images[0]

# print(page_1.extract_text()) #para extrair texto do pdf
# print(page_1.images[0])

# with open(PASTA_NOVA / imagem_1.name, 'wb') as imagem: # para salvar a imagem em uma pasta
#     imagem.write(imagem_1.data)

writer = PdfWriter()
writer.add_page(page_1)

# with open(PASTA_NOVA / 'page_1.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore