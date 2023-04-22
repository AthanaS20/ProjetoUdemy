def soma(*args):
    total = 0 #Criando um acumulador
    for numeros in args:
         total += numeros # somando o acumulador com o indice
    return total 

numeros_salvos = 2, 5, 8, 6
soma_1 = soma(*numeros_salvos) # Desempacotamos os valores para enviar para uma função, nesse caso sum. 
#print(numeros_salvos)
print(sum(numeros_salvos))
