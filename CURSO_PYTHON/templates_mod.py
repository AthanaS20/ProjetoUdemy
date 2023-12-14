# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale 
import string
from pathlib import Path
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

CAMINHO_ARQUIVO = Path(__file__).parent / 'mensagem.txt'

def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 13)
dados = dict(
    nome= 'João',
    valor= converte_para_brl(1_234_256),
    data=data.strftime('%d/%m/%Y'),
    empresa='O.M. ',
    telefone='+55 21 95234856'
)

# texto = '''
# Prezado(a) %nome,

# Informamos que sua mensalidade será cobrada no valor de %{valor} no dia %data. 
# Caso deseje cancelar o serviço, entre em contato com a %empresa pelo telefone %telefone.

# Atenciosamente,

# %{empresa},
# '''

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.safe_substitutesubstitute(dados))

