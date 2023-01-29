"""Exemplo de uso do set"""
letras = set() #Usando o set, podemos salvar o que o usuario digitou dentro dessa classe
while True:

    letra = input('Digite uma letra:')
    letras.add(letra)

    if 'l' in letras:
        print('ACERTOU')
        break
print(letras)
    
