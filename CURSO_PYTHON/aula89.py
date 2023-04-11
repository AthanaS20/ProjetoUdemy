#dir, hasattr e getattr em Python
#dir - lista todos os métodos que podem ser usados na string
string = 'Athana'

print(dir(string))

#hasattr - é usado para checar se determinado método existe ex:

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

#getattr - para chamar o método mesmo se ele estiver em uma variavel

string = 'Athana'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)

