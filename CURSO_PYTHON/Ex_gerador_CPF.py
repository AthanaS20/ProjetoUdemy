"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

"""Primeiro Digito"""
import re 
import sys
cpf_gerado_pelo_usuario = re.sub(
    r'[^0-9]', # considere apenas os numeros de 0 a 9 e nada além deles.
    '', # substitui por nada (aspas sem nada)
    '746.824.890-70' # a string
) #importando o re , basta usar a função re.sub para substituir os traços e espaços
#cpf_gerado_pelo_usuario = '746.824.890-70'.replace('.', '')\
    #.replace('-', '')
# Forma de tratar erro, caso queira tratar apenas numeros substituindo os traços e pontos. .replace('o que quer substituir' , 'pelo oq quer substituir')     


entrada_sequencial = cpf_gerado_pelo_usuario == cpf_gerado_pelo_usuario[0] * len(cpf_gerado_pelo_usuario)
if entrada_sequencial == cpf_gerado_pelo_usuario:
    print('Você digitou números repetidos.') 
    sys.exit() # essa função é usada para sair do python, pode ser usada para encerrar o codigo

cpf_gerado_pelo_usuario = '74682489070'
nove_digitos = cpf_gerado_pelo_usuario[:9] 
contador_regressivo = 10
resultado = 0


for digitos in nove_digitos:
    resultado += int(digitos) * contador_regressivo
    contador_regressivo -= 1
digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0
print(f'O primeiro digito do CPF é {digito}')

"""Segundo digito"""

cpf = '74682489070'
dez_digitos_2 = nove_digitos + str(digito)
contador_regressivo_2 = 11
resultado = 0

for digito_2 in dez_digitos_2:
    resultado += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
ultimo_digito = (resultado * 10) % 11
ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0
print(f'O ultimo digito do CPF é {ultimo_digito}')
novo_cpf_gerado = f'{nove_digitos}{digito}{ultimo_digito}'

"""Validando o CPF"""

if cpf_gerado_pelo_usuario == novo_cpf_gerado:
    print('O CPF digitado é válido.')
else:
    print('O CPF digitado é inválido.')








