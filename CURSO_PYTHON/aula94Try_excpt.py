"""try, except, else, finally"""

try:
    print('ABRIR ARQUIVO')
    #8/0 # caso queira tratar o erro, só criar um except
except ZeroDivisionError as error:
    print(error.__class__.__name__)
# finally sempre será executado, não importando o erro
else:
    # Else é usado quando o programa roda sem nenhum erro
    print('O programa rodou sem erro')
finally:
    print('FECHAR ARQUIVO')