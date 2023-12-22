from time import sleep
from threading import Thread
from threading import Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if quantidade > self.estoque:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque} disponiveis.')
        sleep(1)
        self.estoque -= quantidade
        self.lock.release()


if __name__ == '__main__':
   ingressos = Ingressos(10)
      
   for i in range(1, 10):
       t = Thread(target=ingressos.comprar, args=(i,))
       t.start()
       