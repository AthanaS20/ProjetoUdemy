# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def idade_50_anos(cls, nome):
        return cls(nome, 50)
    
pessoa_1 = Pessoa('Monica', 30)
pessoa_2 = Pessoa.idade_50_anos('Helena')
print(pessoa_2.nome, pessoa_2.idade)