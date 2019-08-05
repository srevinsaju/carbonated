# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 454)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("g960.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.nooc = QtWidgets.QSpinBox(Dialog)
        self.nooc.setGeometry(QtCore.QRect(287, 80, 291, 31))
        self.nooc.setMinimum(1)
        self.nooc.setMaximum(999999999)
        self.nooc.setObjectName("nooc")
        self.bondui = QtWidgets.QSlider(Dialog)
        self.bondui.setGeometry(QtCore.QRect(376, 120, 201, 31))
        self.bondui.setMinimum(1)
        self.bondui.setMaximum(3)
        self.bondui.setPageStep(1)
        self.bondui.setOrientation(QtCore.Qt.Horizontal)
        self.bondui.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.bondui.setTickInterval(1)
        self.bondui.setObjectName("bondui")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(254, 420, 91, 23))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(348, 420, 31, 23))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(68, 420, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.placer = QtWidgets.QSlider(Dialog)
        self.placer.setEnabled(False)
        self.placer.setGeometry(QtCore.QRect(20, 200, 491, 31))
        self.placer.setMinimum(2)
        self.placer.setMaximum(3)
        self.placer.setPageStep(1)
        self.placer.setOrientation(QtCore.Qt.Horizontal)
        self.placer.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.placer.setTickInterval(1)
        self.placer.setObjectName("placer")
        self.placertxt = QtWidgets.QTextEdit(Dialog)
        self.placertxt.setEnabled(False)
        self.placertxt.setGeometry(QtCore.QRect(520, 200, 61, 31))
        self.placertxt.setObjectName("placertxt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 0, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 371, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 60, 571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setPixmap(QtGui.QPixmap("g960.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.abt = QtWidgets.QPushButton(Dialog)
        self.abt.setGeometry(QtCore.QRect(14, 420, 31, 23))
        self.abt.setToolTipDuration(2)
        self.abt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ss-branding.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abt.setIcon(icon2)
        self.abt.setObjectName("abt")
        self.output = QtWidgets.QLabel(Dialog)
        self.output.setGeometry(QtCore.QRect(20, 310, 561, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output.setFont(font)
        self.output.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(63, 63, 63);")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setWordWrap(True)
        self.output.setObjectName("output")
        self.bondtxt = QtWidgets.QLabel(Dialog)
        self.bondtxt.setGeometry(QtCore.QRect(290, 123, 71, 21))
        self.bondtxt.setAutoFillBackground(False)
        self.bondtxt.setStyleSheet("border-color: rgb(117, 117, 117);\n"
"gridline-color: rgb(117, 117, 117);\n"
"background-color: rgb(212, 212, 212);")
        self.bondtxt.setTextFormat(QtCore.Qt.AutoText)
        self.bondtxt.setAlignment(QtCore.Qt.AlignCenter)
        self.bondtxt.setObjectName("bondtxt")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 230, 361, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 250, 361, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 270, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 270, 61, 31))
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.output_2 = QtWidgets.QLabel(Dialog)
        self.output_2.setGeometry(QtCore.QRect(20, 370, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_2.setFont(font)
        self.output_2.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(63, 63, 63);")
        self.output_2.setText("")
        self.output_2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_2.setWordWrap(True)
        self.output_2.setObjectName("output_2")
        self.output_3 = QtWidgets.QLabel(Dialog)
        self.output_3.setGeometry(QtCore.QRect(20, 320, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_3.setFont(font)
        self.output_3.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(63, 63, 63,0);")
        self.output_3.setText("")
        self.output_3.setAlignment(QtCore.Qt.AlignCenter)
        self.output_3.setWordWrap(True)
        self.output_3.setObjectName("output_3")
        self.output_4 = QtWidgets.QLabel(Dialog)
        self.output_4.setGeometry(QtCore.QRect(20, 330, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_4.setFont(font)
        self.output_4.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(63, 63, 63, 0);")
        self.output_4.setText("")
        self.output_4.setAlignment(QtCore.Qt.AlignCenter)
        self.output_4.setWordWrap(True)
        self.output_4.setObjectName("output_4")
        self.output_6 = QtWidgets.QLabel(Dialog)
        self.output_6.setGeometry(QtCore.QRect(20, 360, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_6.setFont(font)
        self.output_6.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(63, 63, 63, 0);")
        self.output_6.setText("")
        self.output_6.setAlignment(QtCore.Qt.AlignCenter)
        self.output_6.setWordWrap(True)
        self.output_6.setObjectName("output_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "carboncompunds - by srevinsaju"))
        self.pushButton.setText(_translate("Dialog", "COMPUTE"))
        self.pushButton_3.setToolTip(_translate("Dialog", "Place the Bond in Alkene and Alkyne type and then update the equation in the output box"))
        self.pushButton_3.setText(_translate("Dialog", "PLACE BOND && UPDATE EQN"))
        self.label.setText(_translate("Dialog", "carbonic™"))
        self.label_2.setText(_translate("Dialog", "by srevinsaju on https://github.com/srevinsaju/carboncompunds"))
        self.label_4.setText(_translate("Dialog", "Bond : Alkane/Alkene/Alkyne"))
        self.label_3.setText(_translate("Dialog", "Number of Carbon atoms"))
        self.label_5.setText(_translate("Dialog", "Position of Alkene / Alkane bond (can be added on consecutively)"))
        self.abt.setToolTip(_translate("Dialog", "About"))
        self.output.setText(_translate("Dialog", "-- OUTPUT --"))
        self.bondtxt.setText(_translate("Dialog", "ALKANE"))
        self.radioButton.setText(_translate("Dialog", "Enter above details"))
        self.radioButton_2.setText(_translate("Dialog", "Enter the IUPAC name (experimental, only Alkane upto 100)"))
        self.pushButton_4.setText(_translate("Dialog", "GO"))


