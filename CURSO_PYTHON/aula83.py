# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
print(a, b)

pessoas = {
    'nome': 'Aline',
    'sobrenome': 'Silva',
}

a, b = pessoas.values()
print(a,b)