# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana6.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 915)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 281, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 70, 571, 61))
        self.label_2.setStyleSheet(u"color:white;\n"
"\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 241, 41))
        self.label_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-50, 220, 331, 61))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 120, 391, 41))
        self.lineEdit.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(290, 230, 381, 41))
        self.lineEdit_2.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(870, 790, 221, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1100, 790, 151, 51))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(224, 123, 79);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-70, -10, 261, 131))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(570, 150, 331, 61))
        self.label_8.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(560, 220, 331, 61))
        self.label_9.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(900, 160, 381, 41))
        self.lineEdit_3.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(900, 230, 381, 41))
        self.lineEdit_4.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(-50, 290, 331, 61))
        self.label_11.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(290, 310, 381, 41))
        self.lineEdit_6.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setEchoMode(QLineEdit.Normal)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-50, 360, 331, 61))
        self.label_12.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(290, 380, 381, 41))
        self.lineEdit_7.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setEchoMode(QLineEdit.Normal)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 450, 571, 61))
        self.label_5.setStyleSheet(u"color:white;\n"
"\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 20, 771, 61))
        self.label_7.setStyleSheet(u"color:white;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(390, 520, 291, 41))
        self.lineEdit_8.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setEchoMode(QLineEdit.Normal)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(140, 520, 241, 41))
        self.label_13.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(140, 590, 241, 41))
        self.label_14.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(140, 650, 241, 41))
        self.label_15.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(140, 700, 241, 41))
        self.label_16.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(700, 520, 241, 41))
        self.label_17.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(390, 590, 291, 41))
        self.lineEdit_9.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_9.setEchoMode(QLineEdit.Normal)
        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(390, 650, 291, 41))
        self.lineEdit_10.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)
        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(390, 710, 291, 41))
        self.lineEdit_11.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_11.setEchoMode(QLineEdit.Normal)
        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(940, 520, 301, 41))
        self.lineEdit_12.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_12.setEchoMode(QLineEdit.Normal)
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(1000, 570, 181, 61))
        self.pushButton_14.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: red;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 170, 241, 41))
        self.label_10.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(270, 170, 391, 41))
        self.lineEdit_5.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1291, 26))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Registro Due\u00f1o: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Nombre:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">N\u00famero de Tel\u00e9fono:</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Correo Electr\u00f3nico:</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Contrase\u00f1a:</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Direcci\u00f3n de Env\u00edo:</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Tipo de Usuario:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Registro de Mascota:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Formulario de Registro de Paciente y Due\u00f1o", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Nombre Completo:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Especie:</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Raza:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Edad: </p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">ID cliente asociado: </p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Buscar ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Apellido:</p><p align=\"right\"><br/></p></body></html>", None))
    # retranslateUi

