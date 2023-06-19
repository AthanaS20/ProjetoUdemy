# Funções decoradoras e decoradores com classes
def adiciona_repr(class_):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    class_.__repr__ = my_repr
    return class_

@adiciona_repr
class Time:
    def __init__(self,nome):
        self.nome = nome
        
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
brasil = Time('Brasil')
portugal = Time('Portugal')

marte = Planeta('Marte')
terra = Planeta('Terra')

print(brasil)
print(portugal)
print(terra)
print(marte)