from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False
        

    def ligando(self):
        if not self._ligado:
             self._ligado = True
    
    def desligando(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin): #Herança multima
    def ligando(self):
        super().ligando()

        if self._ligado:
            msg = f'{self.nome} está ligado.'
            self.log_sucess(msg)

    def desligando(self):
        super().desligando()

        if not self._ligado:
            msg = f'{self.nome} está desligado.'
            self.log_error(msg)