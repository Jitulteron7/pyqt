
from PyQt6 import QtCore, QtGui, QtWidgets


def welcome(Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1202, 800)
        widget = QtWidgets.QWidget(Dialog)
        widget.setGeometry(QtCore.QRect(680, -20, 531, 821))
        widget.setStyleSheet("background-image: url(./image/left_.jpg);")
        widget.setObjectName("widget")
        widget_2 = QtWidgets.QWidget(Dialog)
        widget_2.setGeometry(QtCore.QRect(-1, -1, 691, 801))
        widget_2.setStyleSheet("background-color:\"white\"")
        widget_2.setObjectName("widget_2")
        widget_3 = QtWidgets.QWidget(widget_2)
        widget_3.setGeometry(QtCore.QRect(10, 10, 111, 81))
        widget_3.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_3.setObjectName("widget_3")
        widget_4 = QtWidgets.QWidget(widget_2)
        widget_4.setGeometry(QtCore.QRect(80, 60, 71, 51))
        widget_4.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_4.setObjectName("widget_4")
        widget_5 = QtWidgets.QWidget(widget_2)
        widget_5.setGeometry(QtCore.QRect(80, 680, 81, 61))
        widget_5.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_5.setObjectName("widget_5")
        widget_6 = QtWidgets.QWidget(widget_2)
        widget_6.setGeometry(QtCore.QRect(10, 710, 101, 81))
        widget_6.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_6.setObjectName("widget_6")
        widget_7 = QtWidgets.QWidget(widget_2)
        widget_7.setGeometry(QtCore.QRect(530, 60, 71, 51))
        widget_7.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_7.setObjectName("widget_7")
        widget_8 = QtWidgets.QWidget(widget_2)
        widget_8.setGeometry(QtCore.QRect(570, 10, 111, 81))
        widget_8.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_8.setObjectName("widget_8")
        widget_9 = QtWidgets.QWidget(widget_2)
        widget_9.setGeometry(QtCore.QRect(530, 690, 71, 51))
        widget_9.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_9.setObjectName("widget_9")
        widget_10 = QtWidgets.QWidget(widget_2)
        widget_10.setGeometry(QtCore.QRect(570, 710, 111, 81))
        widget_10.setStyleSheet("background-image: url(./image/particles-geometric-art-line-dot-dip-pen_31941-148.webp);")
        widget_10.setObjectName("widget_10")
        label = QtWidgets.QLabel(widget_2)
        label.setGeometry(QtCore.QRect(90, 150, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        label.setFont(font)
        label.setStyleSheet("font: 30pt \"Times New Roman\";")
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(widget_2)
        label_2.setGeometry(QtCore.QRect(130, 200, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_3 = QtWidgets.QLabel(widget_2)
        label_3.setGeometry(QtCore.QRect(190, 240, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_3.setFont(font)
        label_3.setStyleSheet("text-align: center;")
        label_3.setObjectName("label_3")
        widget_11 = QtWidgets.QWidget(widget_2)
        widget_11.setGeometry(QtCore.QRect(280, 10, 131, 131))
        widget_11.setStyleSheet("border-image: url(./image/IIT_Guwahati_Logo.svg);")
        widget_11.setObjectName("widget_11")
        pushButton = QtWidgets.QPushButton(widget_2)
        pushButton.setGeometry(QtCore.QRect(260, 360, 181, 61))
        pushButton.setStyleSheet("border-radius:20px;\n"
"background-color:rgb(48, 235, 255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"color:\"white\"")
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(widget_2)
        pushButton_2.setGeometry(QtCore.QRect(210, 500, 281, 61))
        pushButton_2.setStyleSheet("border-radius:20px;\n"
"background-color:rgb(48, 235, 255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"color:\"white\"")
        pushButton_2.setObjectName("pushButton_2")

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        label.setText(_translate("Dialog", "Welcome to IIT G Desktop App"))
        label_2.setText(_translate("Dialog",
                                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco"))
        label_3.setText(_translate("Dialog", "Lorem ipsum dolor sit amet, consectetur "))
        pushButton.setText(_translate("Dialog", "Login"))
        pushButton_2.setText(_translate("Dialog", "Create a new account ?"))

        QtCore.QMetaObject.connectSlotsByName(Dialog)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    welcome(Dialog)
    Dialog.show()
    sys.exit(app.exec())
