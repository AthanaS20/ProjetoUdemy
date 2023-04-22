# Métodos em instâncias de classes Pythom
# Método é uma função que está dentro da classe (resumidamente)

class Carro:
    def __init__(self, nome):
        self.nome = nome
        

    def acelerar(self): # Criando um método para instância
        print(f'{self.nome} está acelerando...')

palio = Carro('Palio')
print(palio.nome)
palio.acelerar() #Chamando o método

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

