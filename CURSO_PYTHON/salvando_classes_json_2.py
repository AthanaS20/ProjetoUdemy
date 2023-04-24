from salvando_classe_json import CAMINHO_ARQUIVO, Pessoa, fazendo_dump
import json



with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    pessoa_1 = Pessoa(**pessoas[0])
    pessoa_2 = Pessoa(**pessoas[1])
    pessoa_3 = Pessoa(**pessoas[2])

    print(pessoa_1.nome, pessoa_1.idade)
    print(pessoa_2.nome, pessoa_2.idade)
    print(pessoa_3.nome, pessoa_2.idade)

