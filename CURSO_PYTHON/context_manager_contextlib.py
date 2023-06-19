# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    #tratando o erro com try, exception e finally
    try:
        print('Abrindo o arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # yield faz a função se tornar um generator
    except Exception as e: # colocando a exceção como e, para ter acesso ao erro
        print('Ocorreu um erro', e)
    finally: # executando a função de fechar o arquivo com finally
        print('Fechando o arquivo')
        arquivo.close()

with my_open('arquivo_contextlib.txt', 'w') as arquivo:
    arquivo.write('Arquivo 1\n', 123) #criando um erro
    arquivo.write('Arquivo 2\n')
    arquivo.write('Arquivo 3\n')
    print('WITH', arquivo)