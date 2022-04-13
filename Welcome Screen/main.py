import sys
from PyQt6.uic import loadUi
import login_screen
import welcome_screen
from PyQt6.QtWidgets import QApplication, QWidget, QDialog,QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()



#main

app = QApplication(sys.argv)
widget = QStackedWidget()
welcome = WelcomeScreen()

widget.addWidget(welcome)

widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")