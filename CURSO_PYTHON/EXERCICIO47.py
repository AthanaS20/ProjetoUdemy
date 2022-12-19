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

palavra_secreta = 'amor'
letras_acertadas = ''
contagem = 0

while True:
    tentativa_usuario = input('Digite apenas uma letra:')
    if len(tentativa_usuario) > 1:
        continue 
    
    if tentativa_usuario in palavra_secreta:
        letras_acertadas += tentativa_usuario
    
    palavra_formada = ''
    
    for letras in palavra_secreta:
        if letras in letras_acertadas:
            palavra_formada += letras
        else:
            palavra_formada += '*'
    print(f'Palavra formada: ', palavra_formada)
    
    if len(palavra_secreta) == len(letras_acertadas):
        break
    contagem += 1
print(f'A palavra secreta é {palavra_secreta}.')
print(f'{contagem} foram os números de tentativas.')

        
        

        
    


        
            




        
        
