# Try, Except, else, e finally
"""Para tratar erros individualmente"""

# a = 18
# b = 0
# c = a / b  # Nesse caso teremos um erro ao tentar dividir numero por zero.

try:
    a = 18
    #b = 0 # Aqui tereos um erro onde a variavel não foi definida.
    c = a / b

except ZeroDivisionError: # O nome do erro "ZeroDivisionError" é uma classe, tratamos individualmente aqui.
    print('Erro de divisão por zero')

except NameError:
    print('Nome b não foi definido') # Tratamos o erro individualmente.

except Exception: # O Exception trata qualquer erro e executa o codigo
    ...

print('CONTINUAR ')

"""Na programação, precisamos tratar os erros e esclerecer o mesmo para manter o codigo limpo. Jamais ocultar o erro."""
