# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#Usando a lógica

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return[
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]

lista_de_estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
unidade_federativa = ['BA', 'SP', 'MG', 'RJ']
print(zipper(lista_de_estados, unidade_federativa))

#Usando recurso zip do python

lista_de_estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
unidade_federativa = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista_de_estados, unidade_federativa)))

#Usando o iter_tools do python

from itertools import zip_longest

lista_de_estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
unidade_federativa = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(lista_de_estados, unidade_federativa, fillvalue= 'Sem cidade'))) 
#Esse recurso pega o maior indice da lista e itera sobre ela
