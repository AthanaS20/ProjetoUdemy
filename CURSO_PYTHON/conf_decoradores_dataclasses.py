from dataclasses import dataclass
# froze=True não permite que você interaja com o atributo da classe
# order=True permite que você use o sorted e ordene

@dataclass(frozen=True, order=True)
class Pessoa:
    nome: str
    idade: int

if __name__ == '__main__':
    lista = [Pessoa('C', 23), Pessoa('B', 21), Pessoa('A', 20)]
    ordenar = sorted(lista, key=lambda p: p.idade) # é possível criar sua própria ordenação com lambda, aqui ordenei por idade.
    print(ordenar)