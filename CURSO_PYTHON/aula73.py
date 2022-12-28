"""Higher order functions
Funções de primeira classe"""

def salutation(msg, name):
    return f'{msg}, {name}'

def exectution(functions, *args):
    return functions(*args)

print(exectution(salutation, 'Bom dia', 'Maria'))

# É possível passar funções como parametros em outras funções