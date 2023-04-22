"""Imprecisão de numeros float
Como contonar """
import decimal #Essa biblioteca converte uma string para numero int, é mt usada quando tem numeros floats extensos.

numero_1 = decimal.Decimal('1.050')
numero_2 = decimal.Decimal('0.80')
numero_3 = numero_1 + numero_2
print(f'{numero_1:.2f}') # Dessa forma vc pode escolher quantas casas decimais deseja
print(round(numero_1, 2)) # Função round: primeiro a varaivel e dps o nunmero de casas decimais
print(numero_3)
