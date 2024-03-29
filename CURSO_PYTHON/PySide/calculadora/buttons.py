from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout
from enviroment import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font =  self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setMinimumSize(75, 75)
        self.setFont(font)
        

class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask  = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid() # assim que a classe for chamada no main, ele executa esse metodo.

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, b_text in enumerate(row):
                button = Button(b_text)

                if button not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                
                self.addWidget(button, i, j)

    
    