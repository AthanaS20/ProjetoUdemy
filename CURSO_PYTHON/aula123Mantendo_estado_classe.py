# Mantendo o estado da classe

class Camera:
    def __init__(self, marca, filmando = False):
        self.marca = marca
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.marca} já está filmando...')
            return
        
        print(f'A {self.marca} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.marca} não pode fotograr enquanto filma.')   
    
    def desligar(self):
        print(f'Desligando a {self.marca}...')
        self.filmando = False

        

sony = Camera('Sony')
samsung = Camera('Samsung')

sony.filmar()
sony.filmar()
sony.fotografar()
sony.desligar()
print()
samsung.filmar()