# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []
    
    def inserir_edereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for enderecos in self.endereco:
            print(enderecos.rua, enderecos.numero)
    
    def __del__(self):
        print('APAGANDO', self.nome)
    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO', self.rua,self.numero)

cliente1 = Cliente('Renata')
cliente1.inserir_edereco('Manoel Bandeira', 501)
cliente1.inserir_edereco('Cocota', 5)
print(cliente1.nome)
cliente1.listar_enderecos()



