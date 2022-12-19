"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
'''condicao = 10 == 10
variavel = 'Valor' if condicao else 'outro valor'
print(variavel)'''

'''digito = 9 #  > 9 = 0
novo_digito = digito if digito >= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)'''

# print('Valor' if False else 'Outro valor' if False else 'Fim') - não é recomendado usar varios ifs e elses na mesma linha