# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

"""Minha Solução"""

def multiply(*args):
    total = 1
    for numbers in args:
        total *= numbers
    return total

multiply_numbers = multiply(2, 6, 8, 9, 15)
print(multiply_numbers)
