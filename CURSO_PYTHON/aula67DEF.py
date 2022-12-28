
"""
Valores padrão para parametros
Ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja enviado
para o parametro, o valor padrão será usado.
Refatorar = editar o código
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} y={y} {z=}', x + y + z)
    else:
        print(f'{x=} y={y}', x + y)


soma(1, 2, 3)
soma(2, 3)
soma(5, 6, 8)
