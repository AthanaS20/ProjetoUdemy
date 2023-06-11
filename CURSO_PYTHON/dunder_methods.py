# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    # retornando uma string com dunder str
    # def __str__(self):
    #     return f'{__class__.__name__} ({self.x}, {self.y})'
    
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r}, z={self.z!r})'
# O rper é a representação do seu objeto, utilizado por devs.
# Para passar todos as representações corretas, é recomendável usar !r.

p1 = Ponto(2, 5)
p2 = Ponto(56, 45)
print(p1)
print(repr(p2)) #para retornar o repr caso esteja usando __str__ também