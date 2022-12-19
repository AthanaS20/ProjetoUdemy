"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'cavalo'
letra_acertada_pelo_usuario = ''

while True:
    letra_usuario = input('Digite apenas uma letra: ')

    if len(letra_usuario) > 1:
        continue
    
    if letra_usuario in palavra_secreta:
        letra_acertada_pelo_usuario += letra_usuario
    
    letras_formadas = ''

    for letras in palavra_secreta:
        if letras in letra_acertada_pelo_usuario:
            letras_formadas += letras
            
        else:
            letras_formadas += '*'
            
    print('Palavra formada: ', letras_formadas)
    



    