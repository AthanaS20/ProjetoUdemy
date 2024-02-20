import sys

from main_window import (MainWindow)
from style import setupTheme
from info import Info
from display import Display
from buttons import Button, ButtonsGrid

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,
                               QLabel)

if __name__ == '__main__':

    #Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    # label_txt = QLabel('')
    # label_txt.setStyleSheet('font-size: 100px;')
    # window.addWidgetToVLayout(label_txt)
  

    #Definindo o icone
    # icon = QIcon(str(WINDOW_ICON_PATH))
    # window.setWindowIcon(icon)
    # app.setWindowIcon(icon)

    #Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    #Criando display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttons_grid = ButtonsGrid()
    window.vLayout.addLayout(buttons_grid)

    #Buttons
    button = Button()
    # buttons_grid.addWidget(button)

    

    #label
    label = QLabel()
    window.addWidgetToVLayout(label)

    
    # Executa o programa
    window.adjustFixedSize()
    window.show()
    app.exec()