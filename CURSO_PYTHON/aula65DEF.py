"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
#def varivael():
'''def multiplicacao():
    print(2*1)
    print(2*2)
    print(2*3)
    print(2*4)
multiplicacao()'''

'''def imprimir(a, b, c): # dentro dos parenteses, passamos o parametro 
    print(a, b, c) # para usar os valores dos parametros, basta passar dentro do def

imprimir(2, 3, 4) # Aqui chamanos a função com argumentos'''

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')
    print('=-' * 20)
    

saudacao('Athana')
saudacao('Marcos')
saudacao('Vaca')
saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
