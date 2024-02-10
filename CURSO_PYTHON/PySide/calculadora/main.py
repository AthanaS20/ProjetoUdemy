import sys
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication,
                               QLabel)

from enviroment import WINDOW_ICON_PATH




if __name__ == '__main__':

    #Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    label_txt = QLabel('')
    label_txt.setStyleSheet('font-size: 150px;')
    window.addWidgetToVLayout(label_txt)
    window.adjustFixedSize()

    #Definindo o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)


    # Executa o programa
    window.show()
    app.exec()