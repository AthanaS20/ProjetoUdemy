# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome_carro):
        self._fabricante = None
        self._motor = None
        self.nome_carro = nome_carro

    @property
    def nome_fabrica(self):
        return self._fabricante
    
    @nome_fabrica.setter
    def nome_fabrica(self, fabrica):
        self._fabricante = fabrica

    @property
    def motor_carro(self):
        return self._motor

    @motor_carro.setter
    def motor_carro(self, nome_motor):
        self._motor = nome_motor

        

class Motor:
    def __init__(self, nome):
         self.nome = nome
    

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

carro_1 = Carro('Corsa')
motor_do_carro = Motor('Z500')
fabricante = Fabricante('Chevrolet')
carro_1.motor_carro = motor_do_carro
carro_1.nome_fabrica = fabricante

print('Nome do Carro: ',carro_1.nome_carro)
print('Motor do Carro: ',carro_1.motor_carro.nome)
print('Fabricante: ',carro_1.nome_fabrica.nome)
print( )


print('=-' * 10)
print( )

carro_2 = Carro('KA')
motor_do_carro_2 = Motor('Rocam')
fabricante_2 = Fabricante('Ford')
carro_2.motor_carro = motor_do_carro_2
carro_2.nome_fabrica = fabricante_2

print('Nome do Carro: ',carro_2.nome_carro)
print('Motor do Carro: ',carro_2.motor_carro.nome)
print('Fabricante: ',carro_2.nome_fabrica.nome)
