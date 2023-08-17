"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança) - Feito
    Pessoa tem nome e idade (com getters) - Feito
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca) - Feito
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta - Feito
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito - Feito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar) - Feito
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    
    def __init__(self):
        ...
           
    @abstractmethod
    def sacar_dinheiro(self, valor: float) -> None:
        ...
    
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    #getter_setter abaixo
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome_usuario):
        self._nome = nome_usuario
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade_usuario):
        self._idade = idade_usuario
    
class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    #Metodo para depósito
    def deposito(self, valor):
        if self.deposito:
            return self.saldo + self.deposito
    

    def limite_extra(self, saldo):
        if self.saldo <= 0:
            print(f'Você tem 100,00R$ de limite extra.')
            return saldo + 100
   

    #Implementando metodo abstrato para sacar dinheiro
    def sacar_dinheiro(self, valor):
        if self.valor < self.saldo:
            print('Saque negado, você não tem saldo suficiente')
        else:
            print(f'Saque de {self.valor} R$ realizado.')    
        

        
class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    #Implementando metodo abstrato para sacar dinheiro
    def sacar_dinheiro(self, valor):
        if self.valor < self.saldo:
            print('Saque negado, você não tem saldo suficiente')
        
        else:
            print(f'Saque de {self.valor} R$ realizado.')
        


class Banco:
    def autenticar_agencia(self):
        ...
        

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    




usuario_1 = Pessoa('Athana', 23)
usuario_1.nome = 'Carlos'
print(usuario_1.nome)
conta = ContaCorrente(123, 0)
poupanca = ContaPoupanca(365)
conta.sacar_dinheiro()
poupanca.sacar_dinheiro()
cliente1 = Cliente('Adriana', 23)
cliente1.corrente = conta #Agregação conta corrente
print(cliente1.nome, cliente1.idade, cliente1.corrente)
conta.deposito(23)
conta.limite_extra(0)
