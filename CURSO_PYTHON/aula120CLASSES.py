# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...

pessoa_1 = Pessoa() # Aqui estamos criando uma nova instância da classe
pessoa_1.nome = 'Athana' # Estamos criando um atributo para classe, basta chamar a variavel .atributo da classe
pessoa_1.sobrenome = 'Silva' 
print(pessoa_1.nome) # imprimindo o atributo que foi criado

pessoa_2 = Pessoa() 
pessoa_2.nome = 'Mariana'
pessoa_2.sobrenome = 'Santana'
print(pessoa_2.nome)

############## Forma mais simples 
# O __init__ faz com que atributo criado seja o primeiro a ser iniciado
class Pessoa:
    def __init__(self, nome, sobrenome): #self reserva, nome é o primeiro atributo e sobrenome o segundo
        self.nome = nome
        self.sobrenome = sobrenome

pessoa1 = Pessoa('Athana', 'Silva') 
pessoa2 = Pessoa('Maria', 'Silva')

print(pessoa1.nome, pessoa2.sobrenome)
print(pessoa2.nome, pessoa2.sobrenome)