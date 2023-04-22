# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# Aumente os preços dos produtos a seguir em 10%
for i, k in enumerate(produtos):
    print(f'{k["nome"]} Com acrescimo de 10%: ')
    print(f"{k['preco'] + 1.10:.2f} R$")
    

# Ordene os produtos por nome decrescente (do maior para menor)
#print(produtos['nome'].sort(reverse=True))
import copy
import pprint
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_preco = copy.deepcopy(produtos)


print((sorted(produtos_ordenados_por_preco, key= lambda dicionario: dicionario['preco'])))
print( )
print((sorted(produtos_ordenados_por_nome, key= lambda dicionario: dicionario['nome'], reverse=True)))
