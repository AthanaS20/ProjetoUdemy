"""Retorno de valores das funções
Return - é usado para retornar valores de algumas funções, o que não é o caso do print, que apenas mostra na tela e retorna None"""

def soma(x, y):
    return x + y
    # Abaixo do return não podemos executar nenhum cod, pq o return para a execução de tudo e retorna um valor

soma1 = soma(3, 5)
soma2 = soma(10, 6)
print(soma1 + soma2)