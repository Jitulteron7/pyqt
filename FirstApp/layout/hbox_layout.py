import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("../icon.jpg"))
        self.setGeometry(500, 300, 500, 500)

        hvbox = QHBoxLayout()

        btn1 = QPushButton("Button one")
        btn2 = QPushButton("Button two")
        btn3 = QPushButton("Button three")
        btn4 = QPushButton("Button four")

        hvbox.addWidget(btn1)
        hvbox.addWidget(btn2)
        hvbox.addWidget(btn3)
        hvbox.addWidget(btn4)

        self.setLayout(hvbox)


app = QApplication( [] )

window = Window()
window.show()
sys.exit(app.exec())