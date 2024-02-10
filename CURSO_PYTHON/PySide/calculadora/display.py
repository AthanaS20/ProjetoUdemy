from PySide6.QtWidgets import QLineEdit
from enviroment import BIGGEST_FONT_SIZE, TEXT_MARGIN
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        # margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIGGEST_FONT_SIZE}px;')
        self.setMinimumHeight(BIGGEST_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(15, 15, 15, 15)
