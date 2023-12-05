# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# Import fungsi-fungsi yang diperlukan dari main.py
from main import encrypt_image, save_file


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1073, 587)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(890, 380, 93, 28))
        self.pushButton.setStyleSheet("font: 63 9pt \"Bahnschrift SemiBold SemiConden\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(20, 170, 201, 191))
        self.frame_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-width : 2px;\n"
                                   "border-style:inset;\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(350, 330, 351, 28))
        self.lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-width : 1.2px;\n"
                                    "border-style:inset;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(830, 170, 201, 191))
        self.frame_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border-width : 2px;\n"
                                   "border-style:inset;\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 380, 93, 28))
        self.pushButton_2.setStyleSheet("font: 63 9pt \"Bahnschrift SemiBold SemiConden\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 380, 93, 28))
        self.pushButton_3.setStyleSheet("font: 63 9pt \"Bahnschrift SemiBold SemiConden\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 380, 93, 28))
        self.pushButton_4.setStyleSheet("font: 63 9pt \"Bahnschrift SemiBold SemiConden\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 130, 81, 31))
        self.label.setStyleSheet("background-color: none;\n"
                                 "font: 25 italic 16pt \"Segoe UI Light\";\n"
                                 "text-decoration: underline;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(890, 130, 91, 31))
        self.label_2.setStyleSheet("background-color: none;\n"
                                   "color: rgb(255,255,255);\n"
                                   "font: 25 italic 16pt \"Segoe UI Light\";\n"
                                   "text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 290, 41, 31))
        self.label_3.setStyleSheet("background-color: none;\n"
                                   "font: 25 italic 12pt \"Segoe UI Light\";\n"
                                   "text-decoration: underline;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 20, 421, 31))
        self.label_4.setStyleSheet("background-color: none;\n"
                                   "font: 81 11pt \"Rockwell Extra Bold\";")
        self.label_4.setObjectName("label_4")
        self.label_image_before = QtWidgets.QLabel(Form)
        self.label_image_before.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_image_before.setObjectName("label_image_before")
        self.label_image_after = QtWidgets.QLabel(Form)
        self.label_image_after.setGeometry(QtCore.QRect(880, 220, 151, 151))
        self.label_image_after.setObjectName("label_image_after")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Save File"))
        self.pushButton_2.setText(_translate("Form", "Encrypt"))
        self.pushButton_3.setText(_translate("Form", "Decrypt"))
        self.pushButton_4.setText(_translate("Form", "Upload File"))
        self.label.setText(_translate("Form", "IMAGE"))
        self.label_2.setText(_translate("Form", "RESULT"))
        self.label_3.setText(_translate("Form", "KEY"))
        self.label_4.setText(_translate(
            "Form", "Encryption Image With AES Algorithm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
