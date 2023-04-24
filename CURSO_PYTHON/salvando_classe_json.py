# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'salvando_classe_json.json'

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

pessoa_1 = Pessoa('Amanda', 'Silva', 36)
pessoa_2 = Pessoa('Clarice', 'Costa', 20)
pessoa_3 = Pessoa('Lucas', 'Gomes', 25)
lista_pessoas = [vars(pessoa_1), vars(pessoa_2), vars(pessoa_3)] # Usando o vars ele retorna um dicionario e dessa forma é possível salvar em json.

def fazendo_dump(): # Colocamos dentro de uma função para adiar a execução do código abaixo
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
            json.dump(lista_pessoas, arquivo, indent=2)

if __name__ == '__main__':
    fazendo_dump()
    print('Esse é o main.') 
# Fiz esse if, pois quando apagava os dados no modulo json, ele resetava com as mesmas informações. Não permitia modificar, com esse
# if consigo alterar os dados no arquivo json.





