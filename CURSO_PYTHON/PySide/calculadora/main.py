import sys
from main_window import MainWindow
from PySide6.QtWidgets import (QApplication,
                               QLabel)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label_txt = QLabel('Meu texto')
    label_txt.setStyleSheet('font-size: 150px;')
    window.v_layout.addWidget(label_txt)
    window.adjustFixedSize()

    window.show()
    app.exec()