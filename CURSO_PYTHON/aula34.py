"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
while condicao:
    nome = input('Seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou')