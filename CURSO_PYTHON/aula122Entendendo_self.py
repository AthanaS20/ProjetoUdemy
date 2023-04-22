# Self - é uma convenção, ou seja, chegou-se a um acordo de que seria usado essa palavra 
# Poderia ser outra, ou pode ser outra
# Self, precisa ser o primeiro paramêtro passado na função
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

"""Isso é a instancia -> fusca"""  #Self é a propria instância da classe, ou seja, self é fusca
fusca = Carro('Fusca')
# O que o python faz quando definimos o self no primeiro paramentro:
Carro.acelerar(fusca) 
# Ao chamar a classe Carro, ela está cru sem os dados que passamos, para isso você precisa informar onde você quer usar esse método.
# acelerar(fusca) fusca é a instância que criamos para classe Carro, assim informamos onde deve ser usado esse metodo. 