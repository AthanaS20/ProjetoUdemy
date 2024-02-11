import sys
from main_window import MainWindow
from display import Display
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,
                               QLabel)

from enviroment import WINDOW_ICON_PATH
from info import Info


if __name__ == '__main__':

    #Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    label_txt = QLabel('')
    label_txt.setStyleSheet('font-size: 150px;')
    window.addWidgetToVLayout(label_txt)
  

    #Definindo o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    #Criando display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)
  
    
  
  


    # Executa o programa
    window.adjustFixedSize()
    window.show()
    app.exec()