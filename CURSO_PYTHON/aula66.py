"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y):
    # Definição da função
    print(f'{x=}  y={y} - x + y =', x+y)

soma(2, 3) 
soma(x = 3, y = 2) # Quando a ordem dos valores importa, precisamos nomear os argumentos, nesse caso invertemos os valores nomeando y = 2 e x = 3