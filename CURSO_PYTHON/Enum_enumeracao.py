# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA','DIREITA']) # Chamando a classe diretamente, o vscode não reconhece a typagem

# fazendo dessa forma, fica mais legível
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto() #enum.auto() enumera automaticamente 
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes, Direcoes(1), Direcoes.ESQUERDA) # membro = Classe(valor), Classe['chave']

def mover(direcao: Direcoes): # Estou dizendo que o parametro é do tipo Direcoes
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    """direcao.DIREITA""" #Aqui o editor reconhece o tipo Direcoes
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
