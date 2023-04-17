# Problemas dos parâmetos mutáveis em funções python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Viviane', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Lucas')
adiciona_clientes('Maria', cliente2)
print(cliente2)

# Se o parametro for mútavel, deve se tomar cuidado, nesse caso a função está criando uma nova lista