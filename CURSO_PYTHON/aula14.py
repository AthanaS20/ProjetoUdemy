# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) #Usando dessa forma,caso o usuario digite outra coisa sem ser numero, o codigo apresenta a causa do erro.
int_numero_2 = int(numero_2) # - forma recomendada

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# Se usarmos int direto no input para fazer a conversão e o usuario digitar outra coisa, o cod vai quebrar sem dar a chance de verificar a causa.
# Ex: int(input('Digite sua idade:')) - forma não recomendada