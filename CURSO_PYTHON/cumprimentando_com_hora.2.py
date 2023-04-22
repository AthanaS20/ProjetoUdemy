horario_do_usuario = input('Digite um horário: ')
horario_float = float(horario_do_usuario)
horario_bom_dia = horario_float >= 00 and horario_float <= 11
horario_boa_tarde = horario_float >= 12 and horario_float <= 17
horario_boa_noite = horario_float >= 18 and horario_float <= 23

if horario_bom_dia:
    print('Olá... Tenha um bom dia!')
elif horario_boa_tarde:
    print('Olá...Tenha uma boa tarde!')
elif horario_boa_noite:
    print('Olá...Tenha uma boa noite!')
else:
    print('Digite um horário válido...')


# Caso o usuario digite algo que não seja numero, seria melhor ter feito o programa com try e except
