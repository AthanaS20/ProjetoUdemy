from abc import ABC, abstractmethod

class Contas(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float =0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar_dinheiro(self, valor: float) -> None:
        ...

    def deposito(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
    
    def detalhes(self, msg: str =''):
        print(f'O seu saldo é {self.saldo:.2f}{msg}')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Contas):
    def sacar_dinheiro(self, valor):
        valor_pos_saque = self.saldo - valor
        

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        
        print('Não foi possível realizar o saque.')
        self.detalhes(f'(SAQUE NEGADO {valor})')

class ContaCorrente(Contas):
    def __init__(self, agencia: int, numero_conta: int, saldo: float =0, limite: float =0):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite
    
    def sacar_dinheiro(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = - self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        
        print('Não foi possível realizar o saque.')
        print(f'Seu limite é {-self.limite}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
     
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'



if __name__ == '__main__':
    # conta_poupanca_1 = ContaPoupanca(111, 222, 100)
    # conta_poupanca_1.sacar_dinheiro(1)
    # conta_poupanca_1.deposito(3)

    conta_corrente_1 = ContaCorrente(111, 222, 100, 200)
    conta_corrente_1.sacar_dinheiro(1)
    conta_corrente_1.deposito(3)
    conta_corrente_1.sacar_dinheiro(400)
    

    
    