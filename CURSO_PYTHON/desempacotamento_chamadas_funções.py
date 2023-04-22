# Desempacontamento em chamadas de métodos e funções

string = 'abcde'
lista = ['Maria', 'Luiza', 1, 2, 3,  'Laura']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
'''a, b, *_, ap, u = lista
print(a, u, ap)'''

print('Maria', 'Luiza', 1, 2, 3, 'Laura')
print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')
