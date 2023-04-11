# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

lista = []
for num in range(10):
    lista.append(num)
#print(lista)

#Usando o list comprehension, da para fazer o mesmo cod de cima em uma linha.

lista = [
    num * 2  
    for num in range(10)
]

#print(lista)

# Mapeamento de dados em list comprehension
import pprint
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

produtos = [
    {**produtos, 'preco': produtos['preco'] * 1.05} 
    if produtos['preco'] > 20 else {**produtos}
    for produtos in produtos
]

#Filtrando dados em list comprehension
produtos = [
    {**produtos, 'preco': produtos['preco'] * 1.05} 
    if produtos['preco'] > 20 else {**produtos}
    for produtos in produtos if produtos['preco'] > 10
]

pprint.pprint(produtos)

#Tudo que vem a esquerda do for é mapeamento, direita 
