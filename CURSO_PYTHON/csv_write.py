from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'csv_write.csv'

lista_clientes = [
    {'Nome': 'Athana', 'Idade': 28, 'Cidade': 'RJ'},
    {'Nome': 'Luana', 'Idade': 25, 'Cidade': 'ES'},
    {'Nome': 'Lucas', 'Idade': 35, 'Cidade': 'BA'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames= nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)


print(lista_clientes[0].keys())