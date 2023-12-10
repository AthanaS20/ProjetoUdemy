import json
import os

NOME_ARQUIVO = 'modulo_json_arquivos.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

movie = {'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
               'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
               'is_movie': True, 
               'imdb_rating': 8.8, 
               'year': 2001, 
               'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
               'budget': None}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(movie, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    json_movie = json.load(arquivo)
    print(json_movie)