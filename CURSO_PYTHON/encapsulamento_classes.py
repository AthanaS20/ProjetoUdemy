# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Foo:
    def __init__(self):
        self.publico = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

        

    def metodo_publico(self):
        self._metodo_protected() # Podemos chamar o metodo protegido dentro do publico, assim está correto.
        print(self.__private)
        return 'o método protected está dentro do método publico'
    
    def _metodo_protected(self):
        return 'metodo protegido'  

    def __metodo_private(self):
        return 'metodo privado'    

f = Foo()
print(f.metodo_publico())
# print(f.metodo_protegido())  # não devemos usar o método protected fora da classe