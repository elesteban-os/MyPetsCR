# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 755)
        MainWindow.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 50, 281, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 170, 241, 31))
        self.label_2.setStyleSheet(u"color:white;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 270, 241, 41))
        self.label_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 330, 161, 31))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 410, 221, 51))
        self.label_5.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 270, 381, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 199, 167);\n"
"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: Black;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(380, 330, 381, 41))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 199, 167);\n"
"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: Black;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 610, 221, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(890, 610, 151, 51))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(224, 123, 79);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 30, 331, 201))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(390, 410, 211, 51))
        self.radioButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 199, 167);\n"
"border-radius:20px;\n"
"color: Black;")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(610, 410, 211, 51))
        self.radioButton_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 199, 167);\n"
"border-radius:20px;\n"
"color: Black;")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(520, 480, 211, 51))
        self.radioButton_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 199, 167);\n"
"border-radius:20px;\n"
"color: Black;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1084, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MiPet", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inicio de Sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Correo Electr\u00f3nico:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Contrase\u00f1a:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Tipo de Usuario:</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salir ", None))
        self.label_6.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Administrador ", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Veterinario", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
    # retranslateUi

