lista_de_compras = []

while True:
    inserir_listar_apagar = input('Selecione uma opção: \n[i]nserir [l]istar [a]pagar:  ').lower()[0]

    if inserir_listar_apagar in 'i':
        produto_inserido = input('Qual o produto deseja inserir na lista? ')
        lista_de_compras.append(produto_inserido)
        continue
    
    if inserir_listar_apagar in 'l':
        for item, valores in enumerate(lista_de_compras):
            print(item, valores)
        if lista_de_compras == []:
            print('Não há nada para listar ainda.')
        continue
        
    
    if inserir_listar_apagar in 'a':
        try:
            apagar_indice = int(input('Escolha um índice para apagar: '))
            del lista_de_compras[apagar_indice]
        except ValueError: # Se o usuario escolher algo que não seja um numero, usamos o valueerror para identificar e informar
            print('Por favor, escolha um número inteiro')
        except IndexError: # Se o usuario escolher algo um indice que n existe, usamos o IndexError para identificar e informar
            print('Índice não existe na lista')
    else:
        print('Favor escolher uma opção válida: [i], [a] ou [l]')

# Minhas resposta
# É importante tratar cada erro para não estourar o código no meio da execução.   