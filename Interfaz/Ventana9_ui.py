# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana9.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1269, 698)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 281, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 550, 221, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(980, 550, 151, 51))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(224, 123, 79);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-50, 10, 261, 131))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 150, 571, 61))
        self.label_5.setStyleSheet(u"color:white;\n"
"\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 30, 771, 61))
        self.label_7.setStyleSheet(u"color:white;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(360, 240, 291, 41))
        self.lineEdit_8.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setEchoMode(QLineEdit.Normal)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(110, 240, 241, 41))
        self.label_13.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 310, 241, 41))
        self.label_14.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(110, 370, 241, 41))
        self.label_15.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(110, 420, 241, 41))
        self.label_16.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(700, 240, 241, 41))
        self.label_17.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(360, 370, 291, 41))
        self.lineEdit_10.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)
        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(360, 430, 291, 41))
        self.lineEdit_11.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_11.setEchoMode(QLineEdit.Normal)
        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(950, 240, 301, 41))
        self.lineEdit_12.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_12.setEchoMode(QLineEdit.Normal)
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(1010, 290, 181, 61))
        self.pushButton_14.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: red;")
        self.comboBoxEspecie = QComboBox(self.centralwidget)
        self.comboBoxEspecie.setObjectName(u"comboBoxEspecie")
        self.comboBoxEspecie.setGeometry(QRect(360, 310, 271, 41))
        self.comboBoxEspecie.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_13 = QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(950, 380, 291, 41))
        self.lineEdit_13.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_13.setEchoMode(QLineEdit.Normal)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(700, 390, 241, 41))
        self.label_18.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_14 = QLineEdit(self.centralwidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(950, 430, 291, 41))
        self.lineEdit_14.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_14.setEchoMode(QLineEdit.Normal)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(700, 420, 241, 41))
        self.label_19.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1269, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MiPet", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Registro de Mascota:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Formulario de Registro de Paciente", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Nombre Completo:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Especie:</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Raza:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Edad: </p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">ID cliente asociado: </p></body></html>", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Buscar ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Alergias:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Padecimientos:</p></body></html>", None))
    # retranslateUi

