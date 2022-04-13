import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("../icon.jpg"))
        self.setGeometry(500, 300, 500, 500)

        grid = QGridLayout()

        btn1 = QPushButton("Button one")
        btn2 = QPushButton("Button two")
        btn3 = QPushButton("Button three")
        btn4 = QPushButton("Button four")
        btn5 = QPushButton("Button five")
        btn6 = QPushButton("Button six")
        btn7 = QPushButton("Button seven")
        btn8 = QPushButton("Button eight")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)
        # grid.addWidget(btn1,0,0)
        # grid.addWidget(btn2,0,1)
        # grid.addWidget(btn3,1,0)
        # grid.addWidget(btn4,1,1)
        # grid.addWidget(btn5,2,0)
        # grid.addWidget(btn6,2,1)
        # grid.addWidget(btn7,3,0)
        # grid.addWidget(btn8,3,1)

        self.setLayout(grid)


app = QApplication( [] )

window = Window()
window.show()
sys.exit(app.exec())