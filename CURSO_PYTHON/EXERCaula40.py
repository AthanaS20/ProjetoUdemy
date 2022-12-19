primeiro_numero_usuario = input('Digite um número inteiro: ')
segundo_numero_usuario = input('Digite um número inteiro: ')
operador_usuario = input('Digite um operador para o calculo: ')
primeiro_numero_usuario_inteiro = int(primeiro_numero_usuario)
segundo_numero_usuario_inteiro = int(segundo_numero_usuario)

contador = 0

while contador < primeiro_numero_usuario_inteiro and contador < segundo_numero_usuario_inteiro:
    if '+' in operador_usuario:
        calculo = (primeiro_numero_usuario_inteiro + segundo_numero_usuario_inteiro)
        
        print(f'A soma de {primeiro_numero_usuario} + {segundo_numero_usuario} = {calculo}')
        break
    if '-' in operador_usuario:
        subtração_calculo = primeiro_numero_usuario_inteiro - segundo_numero_usuario_inteiro
        print(f'A subtração de {primeiro_numero_usuario} - {segundo_numero_usuario} = {subtração_calculo}')
        break
    if '*' in operador_usuario:
        multiplicacao_calculo = primeiro_numero_usuario_inteiro * segundo_numero_usuario_inteiro
        print(f'A multiplicação de {primeiro_numero_usuario} * {segundo_numero_usuario} = {multiplicacao_calculo}')
        break
    if '/' in operador_usuario:
        divisao_calculo = primeiro_numero_usuario_inteiro / segundo_numero_usuario_inteiro
        print(f'A divisão de {primeiro_numero_usuario} / {segundo_numero_usuario} = {divisao_calculo:.2f}')
        break
    

# Minha resposta
