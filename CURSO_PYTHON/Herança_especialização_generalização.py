# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, __class__.__name__)


class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...

cliente_1 = Cliente('Maria', 'Helena')
cliente_1.falar_nome_classe()
aluno = Aluno('Alexandre', 'Pires')
aluno.falar_nome_classe()