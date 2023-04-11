# Try, Except, else, e finally
"""Para tratar erros individualmente"""

# a = 18
# b = 0
# c = a / b  # Nesse caso teremos um erro ao tentar dividir numero por zero.

try:
    a = 18
    #b = 0 # Aqui tereos um erro onde a variavel não foi definida.
    c = a / b

except ZeroDivisionError: 
    ...

except NameError as e: 
    print(e.__class__.__name__) 

except (TypeError, IndexError) as error: # Usamos o as error para mostrar o nome do erro na tela.
    print('TypeError + IndexError') # Podemos tratar dois erros na mesma linha, criando uma tupla.
    print('MSG: ', error)

except Exception: 
    ...

print('CONTINUAR ')