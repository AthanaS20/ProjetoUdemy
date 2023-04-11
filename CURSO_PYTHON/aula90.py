# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__

#Generator - são funções que você consegue pausar 
# Caso você precise acessar um item em uma lista muito grande, usando o generator você consegue
#pausar e solicitar o que vc quer.

# generator = [n for n in range(10)] #Se a range fosse aé 10000 esse numero ficaria salvo na memoria
# print(generator)
generator = (n for n in range(10)) # para usar o generator, basta usar parenteses 
print(next(generator))
print(next(generator))

#Usando o for ele entrega item por item sem salvar tudo na memoria
for n in generator:
    print(n)

#A desvantagem é que não se pode acessar os indices, saber o tamanho, o último indice, etc.