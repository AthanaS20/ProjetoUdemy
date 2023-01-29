def executa(funcao, *args):
    return funcao(*args)



#Usando lambda
def soma(x, y):
    return x + y

print(

    executa(
        lambda x, y: x + y, 2, 5
    )
)



def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#Usando lambda
duplica = executa(
    lambda m: lambda n: n * m, 2
)
print(duplica(2))