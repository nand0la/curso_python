import sys

from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,
    QWidget,
    QGridLayout,
)

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Text Btn')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    
    app = App()
    app.show()

    qt.exec_()