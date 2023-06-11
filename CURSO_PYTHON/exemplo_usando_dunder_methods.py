class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
   
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name} ({self.x!r}, {self.y!r})'
    
    # Usando o magic method que soma os valores recebidos
    def __add__(self, other):
        novo_x = self.x + self.y
        novo_y = other.x + other.y
        return Ponto(novo_x, novo_y)
    # usando o magic method gt que verifica se um valor é maior que outro
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    
# rodando o código que verifica   
if __name__ == '__main__':
    p1 = Ponto(2, 5)
    p2 = Ponto(10, 5)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2', p1 > p2)
    print('P2 é maior que P1', p2 > p1)


