"""Crie uma função que fala se o número é par ou ímpar
Retorne se o número é par ou ímpar"""

# Minha solução

def number(x):
    if x % 2 == 0:
        return 'Number is pair'
    else:
        return 'Number is odd'

result = number(11)
print(result)

# Nota: O uso do else é redundante nesse caso, porque se a primeira condição for verdeira o return n vai executar a segunda condição.
"""O código deveria ficar assim:"""
def number(x):
    if x % 2 == 0:
        return 'Number is pair'
    return 'Number is odd'

result = number(11)
print(result)
        
