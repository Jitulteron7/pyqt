import sys
from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("icon.jpg"))
        # self.setFixedWidth(600)
        # self.setFixedHeight(800)
        self.setGeometry(500,300,500,500)
        # self.setStyleSheet('background-color:#7EBCFF')

        stylesheet = (
            'background-color:#7EBCFF'
        )
        self.setStyleSheet(stylesheet)


app = QApplication([])

window =Window()
window.show()
sys.exit(app.exec())