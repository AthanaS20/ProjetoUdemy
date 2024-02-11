from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from enviroment import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, text: str, parent: None | QWidget = None) -> None: 
        super().__init__(text, parent)
        self.configStyleInfo()
    
    def configStyleInfo(self):
        self.setStyleSheet(f'{SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

