# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout, 
                               QGridLayout, QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

button = QPushButton('Text of button')
button.setStyleSheet('font-size: 40px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')


layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)


@Slot()
def slot_example(status_bar):
    status_bar.showMessage('The slot was open')
    
@Slot()
def slot_2(checked):
    print('Is checked?', checked)

@Slot()
def third_slot(action):
    def inner():
        slot_2(action.isChecked())
    return inner

#status bar
status_bar = window.statusBar()
status_bar.showMessage('Status bar message')

#menu bar
menu = window.menuBar()
first_menu = menu.addMenu('First menu')
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(lambda: slot_example(status_bar))

# second_menu = menu.addMenu('Second menu')
second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(slot_2)
second_action.hovered.connect(third_slot(second_action))

button.clicked.connect(third_slot(second_action))



window.show()
app.exec()