from PySide6.QtWidgets import QPushButton, QWidget
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
        self.setProperty('cssClass', 'specialButton')


    
    