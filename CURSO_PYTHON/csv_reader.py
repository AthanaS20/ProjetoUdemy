

from pathlib import Path
import csv


CAMINHO_CSV = Path(__file__).parent / 'Clientes.csv'

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha)