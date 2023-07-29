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
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
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
    @abstractmethod
    def __init__(self, conta_corrente: int, conta_poupanca: int):
        self.conta_corrente = conta_corrente
        self.conta_poupanca = conta_poupanca
    
    @property
    def conta_corrente(self):
        return self.conta_corrente
    @property
    def conta_poupanca(self):
        return self.conta_poupanca

    @conta_corrente.setter 
    @abstractmethod
    def conta_corrente(self, conta_corrente): ...

    @conta_poupanca.setter
    @abstractmethod
    def conta_poupanca(self, conta_poupanca):...

class Pessoa(ABC):
    def __init__(self, nome, idade):
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
    def __init__(self, conta_corrente):
        super().__init__(conta_corrente)

    @Conta.conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        self.conta_corrente = conta_corrente
        
class ContaPoupanca(Conta):
    def __init__(self, conta_poupanca):
        super().__init__(conta_poupanca)
    
    @Conta.conta_poupanca.setter
    def conta_poupanca(self, conta_poupanca):
        self.conta_poupanca = conta_poupanca
        


class Banco:
    pass

class Cliente(Pessoa):
    def __init__(self):
        ...


usuario_1 = Pessoa('Athana', 23)
usuario_1.nome = 'Carlos'
print(usuario_1.nome)
conta = ContaCorrente(123)
print(conta.conta_corrente)