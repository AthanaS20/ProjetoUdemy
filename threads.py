from time import sleep
from threading import Thread

# class MyThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()
    
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MyThread('Hello, World', 5)
# t1.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# outra forma de usar threads

def demorar(texto, tempo):
    sleep(tempo)
    print(texto)
t = Thread(target=demorar, args=('Olá, fulano', 10))
t.start()

while t.is_alive():
    print('Esperando Thread...')
    sleep(2)