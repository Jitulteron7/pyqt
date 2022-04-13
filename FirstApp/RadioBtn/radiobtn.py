import sys
from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout, QGroupBox, QLabel, QRadioButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IIT Project")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setGeometry(500, 300, 500, 500)

        vbox = QVBoxLayout()
        self.radio_btn()
        vbox.addWidget(self.grpbox)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Times New Roman",15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)



    def radio_btn(self):
        self.grpbox = QGroupBox("Choose programming language")
        self.grpbox.setFont(QFont("Times New Roman",15))

        hbox = QHBoxLayout()

        self.btn_radio1 =  QRadioButton("Python")
        self.btn_radio1.setChecked(True)
        self.btn_radio1.setFont(QFont("Times New Roman",14))
        self.btn_radio1.toggled.connect(self.on_selected)
        hbox.addWidget(self.btn_radio1)

        self.btn_radio2 = QRadioButton("C++")
        self.btn_radio2.setFont(QFont("Times New Roman", 14))
        self.btn_radio2.toggled.connect(self.on_selected)
        hbox.addWidget(self.btn_radio2)

        self.btn_radio3 = QRadioButton("JAVA")
        self.btn_radio3.setFont(QFont("Times New Roman", 14))
        self.btn_radio3.toggled.connect(self.on_selected)
        hbox.addWidget(self.btn_radio3)


        self.grpbox.setLayout(hbox)

    def on_selected(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText("You have selected: " + radio.text())

app = QApplication([])

window =Window()
window.show()
sys.exit(app.exec())