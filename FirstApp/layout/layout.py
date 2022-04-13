import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("../icon.jpg"))
        self.setGeometry(500, 300, 500, 500)

        vbox = QVBoxLayout()

        btn1 = QPushButton("Button one")
        btn2 = QPushButton("Button two")
        btn3 = QPushButton("Button three")
        btn4 = QPushButton("Button four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)


app = QApplication( [] )

window = Window()
window.show()
sys.exit(app.exec())