# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) - faz uma cópia dos itens imútaveis
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy # Caso queira copiar todo o dicionario incluindo mutáveis e imutaveis, basta importar copy e usar o deepcopy

dict_1 = {
    'key1': 1,
    'key2': 2,
    'list1': [2,3,5],

}

dict_2 = copy.deepcopy(dict_1) 

dict_2['key1'] = 1000
dict_2['list1'][1] = 542

print(dict_1)
print(dict_2)