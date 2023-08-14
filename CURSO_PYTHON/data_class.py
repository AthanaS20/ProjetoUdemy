# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

class Pessoa:
  nome: str
  idade: int

if __name__ == '__main__':
  pessoa1 = Pessoa('Athana', 27)
  pessoa2 = Pessoa('Athana', 27)
  print(pessoa1 == pessoa2) # metodo __eq__() comparação, nesse caso apontaria True, porque tem os mesmo atributos.
