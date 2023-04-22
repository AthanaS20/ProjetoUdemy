# Atributo de classe

class Pessoa:
    ano_atual = 2023 # é usado quando se quiser fixar valores para uma classe especifica, nesse caso para calcular o ano de nascimento
    #precisamos do ano atual.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

pessoa_1 = Pessoa('Athana', 27)
pessoa_2 = Pessoa('Cleyson', 23)

print(pessoa_1.get_ano_nascimento())
print(pessoa_2.get_ano_nascimento())