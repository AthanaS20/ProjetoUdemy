nome_do_usuario = input('Digite seu nome: ')
nome_tamanho_curto = len(nome_do_usuario) <= 4
nome_tamanho_normal = len(nome_do_usuario) >= 5 and len(nome_do_usuario) <= 6
nome_tamanho_grande = len(nome_do_usuario) > 6

if nome_tamanho_curto:
    print(f'Seu nome é {nome_do_usuario} possui {len(nome_do_usuario)} letras e tem tamanho curto.')
elif nome_tamanho_normal:
    print(f'Seu nome é {nome_do_usuario}, possui {len(nome_do_usuario)} letras e tem tamanho normal.')
elif nome_tamanho_grande:
    print(f'Seu nome é {nome_do_usuario}, tem {len(nome_do_usuario)} letras e tem tamanho grande.')