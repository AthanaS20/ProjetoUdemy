# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...
class AnotherError(Exception):
    ...
def raising():
    exception = MyError('a', 'b', 'c')
    exception.add_note('Olha a nota 1...')
    exception.add_note('Adicionando nota ao erro para comunicar algo...')
    raise exception

try:
    1/0
    raising()
except (MyError, ZeroDivisionError) as error:
    print(f'{error} esse erro está vindo de: ')
    print(error.__class__.__name__)
    print( )
    exception = AnotherError('I will raise again.')
    exception.add_note('Adicionando nota ao erro para comunicar algo...')
    raise exception from error
    # raise #Relançando a exceção 