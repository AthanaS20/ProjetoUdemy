# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador): # criar uma função que recebe como parametro q qntdade de vezes que vamos multiplicar
    def multiplicar(numero): 
        return numero * multiplicador
    return multiplicar
        
duplicar_numero = criar_multiplicador(2)
triplicar_numero = criar_multiplicador(3)
quadruplicar_numero = criar_multiplicador(4)

print(duplicar_numero(2))
print(triplicar_numero(5))
print(quadruplicar_numero(4))
    
    
      


