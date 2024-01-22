# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets


import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout

app = QApplication(sys.argv)
button = QPushButton('Text of button')
button.setStyleSheet('font-size: 40px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')


central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)

central_widget.show()
app.exec()