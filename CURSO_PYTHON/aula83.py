# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoas = {
    'nome': 'Aline',
    'sobrenome': 'Silva',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoas, **dados_pessoa} #para extrair informação do dicionario, basta abrir chaves e usar 2 '*'
# print(pessoa_completa)

def mostrar_argumentos_nomeados(*args, **kwargs): #kwargs é para parametros nomeados e args, não nomeados.
    for chave, valor in kwargs.items():
        print(chave, valor)


mostrar_argumentos_nomeados(nome ='Ana', idade= 17) #Pode substituir o valor do dicionario, nomeando 
mostrar_argumentos_nomeados(**pessoa_completa)# desempacontando todo o dicionario 