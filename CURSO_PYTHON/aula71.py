"""args - Argumentos não nomeados
- *args (empacotamento e desempacotamento"""

#Lembrete de desempacotamento

x, y, *resto = 1, 2, 3, 4 # Nesse caso o x recebe valor 1  y valor 2, o restante salvamos no *resto 
print(x, y, resto) # e desempacotamos aqui se for necessário.

def soma(*args): # Estamos empacotando argumentos não nomeados, oq da a possibilidade de trabalhar com muitos valores.
    print(args)

soma(2, 5, 5, 8)

# Por ser uma tupla o arg é imutável, caso queira alterar um valor basta converter para lista
def soma(*args):
    args = list(args) 
soma(2, 5, 5, 8)

# Somando com for
def soma(*args):
    total = 0 #Criando um acumulador
    for numeros in args:
        total = total + numeros # somando o acumulador com o indice
        print(total)
soma(1, 2, 6, 8, 7, 2)

