import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtGui import QIcon,QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setGeometry(500,300,500,500)
        self.create_widget()

    def create_widget(self):
        btn = QPushButton("Click Me",self)
        # btn.move(220,150)
        btn.setGeometry(100,100,120,50)
        btn.setStyleSheet('background-color:red')
        btn.setIcon(QIcon('icon.jpg'))
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel("My Label",self)
        self.label.move(300,300)
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont("Times New Roman",15))

    def clicked_btn(self):
        self.label.setText("Text is changed")
        self.label.setStyleSheet("background-color:red")

app = QApplication([])

window =Window()
window.show()
sys.exit(app.exec())