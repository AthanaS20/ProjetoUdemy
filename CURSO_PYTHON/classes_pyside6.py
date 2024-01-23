# Working with class PySide6

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout, 
                               QGridLayout, QMainWindow)





class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        
        self.button = self.make_button('Text of button')  
        self.button.clicked.connect(self.slot_2)       
        self.button2 = self.make_button('Text of button 2')
        self.button3 = self.make_button('Text of button 3')

      
        

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)
        self.layout.addWidget(self.button, 1, 1, 1, 1)
        self.layout.addWidget(self.button2, 1, 2, 1, 1)
        self.layout.addWidget(self.button, 1, 3, 1, 2)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)
        self.layout.addWidget(self.button, 1, 1)
        self.layout.addWidget(self.button2, 1, 2) 

        #status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Status bar message')

        #menu bar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('First menu')
        self.first_action = self.first_menu.addAction('First Action')
        self.first_action.triggered.connect(self.slot_example)

        # second_menu = menu.addMenu('Second menu')
        self.second_action = self.first_menu.addAction('Second Action')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.slot_2)
        self.second_action.hovered.connect(self.slot_2)   

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('The slot was open')
    
    @Slot()
    def slot_2(self):
        print('Is checked?', self.second_action.isChecked())
    
    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 30px')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()