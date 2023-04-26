# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    def get_cor(self):
        return self.cor_tinta
# um exemplo de uso do get, é alterar querer alterar o nome do atributo da classe, porém em um código extenso seria impossível, então
# usando o get, você só precisa alterar em um local.

caneta_1 = Caneta('Azul')
print(caneta_1.get_cor())
print(caneta_1.get_cor())
print(caneta_1.get_cor())
print(caneta_1.get_cor())

################################

# o property faz o metodo se comportar como um atributo
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta

caneta_1 = Caneta('Rosa')
print(caneta_1.cor) # chamamos o metodo cor sem (), pois ele se comporta como atribulo por conta do property.

    
        