# Funções decoradoras e decoradores com metodos

def adiciona_repr(class_):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    class_.__repr__ = my_repr
    return class_

# Criando uma função decoradora
def meu_planeta(metodo):
    def metodo_interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if 'Terra' in resultado:
            return 'Você está em casa'

        return resultado
    return metodo_interno
        

@adiciona_repr
class Time:
    def __init__(self,nome):
        self.nome = nome
        
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_planeta(self): # criando um método dentro da classe
        return f'O planeta é {self.nome}'
    
brasil = Time('Brasil')
portugal = Time('Portugal')

marte = Planeta('Marte')
terra = Planeta('Terra')

print(brasil)
print(portugal)
print(terra)
print(marte)