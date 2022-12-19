nome = 'Luana'
tamanho_nome = len(nome)
#print(tamanho_nome)

letra = 0

while letra < len(nome):
    print(nome[letra],end='')
    letra += 1
    traços = 1
    while traços <= tamanho_nome:
        traços += 1
        print('-',end='')
        
        break

    #print(letras)

# Resposta do professor abaixo

    """
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

