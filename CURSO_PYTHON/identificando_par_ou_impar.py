#Programa para identificar se é PAR OU ÍMPAR

numero_inteiro_do_usuario = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_inteiro_do_usuario)
    numero_par = numero_inteiro % 2 == 0
    numero_impar = numero_inteiro % 2 == 1

    if numero_par:
        print(f'O número digitado foi {numero_inteiro} e ele é PAR.')
    elif numero_impar:
        print(f'O número digitado foi {numero_inteiro} e ele é ÍMPAR.')
except:
    print('Desculpe, esse não é um número inteiro.')
    

    

