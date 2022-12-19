"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) #Essa função adiciona algo ao ultimo item da lista
lista.pop() # Essa função remove o último item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # Nessa função você pode escolher qual indice deseja remover, nesse caso o indice 3
print(lista, 'Removido,', ultimo_valor)