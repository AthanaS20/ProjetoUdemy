from abc import ABC, abstractmethod

class Contas(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar_dinheiro(self, valor):
        ...

    def deposito(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f}{msg}')
    
class ContaPoupanca(Contas):
    def sacar_dinheiro(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        
        print('Não foi possível realizar o saque.')
        self.detalhes(f'(SAQUE NEGADO {valor})')


if __name__ == '__main__':
    conta_poupanca_1 = ContaPoupanca(111, 222, 0)
    conta_poupanca_1.sacar_dinheiro(1)
    conta_poupanca_1.deposito(3)

    
    