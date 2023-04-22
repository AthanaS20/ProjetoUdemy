#Escopo da classe
# Dentro do escopo da classe, tem os métodos

class Animal:

    def __init__(self, nome):
        self.nome = nome
    def comendo(self, alimento):
        return f'O {self.nome} está comendo {alimento}'
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal('Leão')
print(leao.nome)
print(leao.executar('maçã'))
