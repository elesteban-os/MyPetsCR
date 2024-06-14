# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExpedienteVet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_ExpedienteDialog(object):
    def setupUi(self, ExpedienteDialog):
        if not ExpedienteDialog.objectName():
            ExpedienteDialog.setObjectName(u"ExpedienteDialog")
        ExpedienteDialog.resize(1291, 744)
        ExpedienteDialog.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(ExpedienteDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(-10, 20, 1301, 741))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 281, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-60, 260, 241, 41))
        self.label_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-150, 380, 331, 61))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 260, 311, 41))
        self.lineEdit.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(200, 390, 311, 41))
        self.lineEdit_2.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(780, 610, 221, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1040, 610, 151, 51))
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
        self.label_8.setGeometry(QRect(410, 250, 331, 61))
        self.label_8.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(400, 320, 331, 61))
        self.label_9.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(750, 260, 321, 41))
        self.lineEdit_3.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(750, 330, 321, 41))
        self.lineEdit_4.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(-150, 440, 331, 61))
        self.label_11.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(200, 460, 311, 41))
        self.lineEdit_6.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setEchoMode(QLineEdit.Normal)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-140, 520, 331, 61))
        self.label_12.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 120, 851, 81))
        self.label_7.setStyleSheet(u"color:white;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-60, 330, 241, 41))
        self.label_10.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(200, 330, 311, 41))
        self.lineEdit_5.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButtonMostrarDatos = QPushButton(self.centralwidget)
        self.pushButtonMostrarDatos.setObjectName(u"pushButtonMostrarDatos")
        self.pushButtonMostrarDatos.setGeometry(QRect(200, 610, 211, 61))
        self.pushButtonMostrarDatos.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(200, 520, 431, 81))
        self.lineEdit_7.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setEchoMode(QLineEdit.Normal)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1040, 60, 151, 51))
        self.pushButton_3.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(224, 123, 79);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(730, 60, 301, 41))
        self.lineEdit_8.setStyleSheet(u"border-radius:10px;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setEchoMode(QLineEdit.Normal)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(390, 50, 331, 61))
        self.label_13.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.menubar = QMenuBar(ExpedienteDialog)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1291, 22))
        self.statusbar = QStatusBar(ExpedienteDialog)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 21))

        self.retranslateUi(ExpedienteDialog)

        QMetaObject.connectSlotsByName(ExpedienteDialog)
    # setupUi

    def retranslateUi(self, ExpedienteDialog):
        ExpedienteDialog.setWindowTitle(QCoreApplication.translate("ExpedienteDialog", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ExpedienteDialog", u"MiPet", None))
        self.label_3.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Nombre:</p><p align=\"right\"><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Alergias:</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("ExpedienteDialog", u"Guardar Cambios ", None))
        self.pushButton_2.setText(QCoreApplication.translate("ExpedienteDialog", u"Cancelar ", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Especie</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Edad:</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Padecimientos:</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Historial</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ExpedienteDialog", u"Expediente Digital", None))
        self.label_10.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Raza:</p></body></html>", None))
        self.pushButtonMostrarDatos.setText(QCoreApplication.translate("ExpedienteDialog", u"Ver ", None))
        self.pushButton_3.setText(QCoreApplication.translate("ExpedienteDialog", u"Buscar", None))
        self.lineEdit_8.setText("")
        self.label_13.setText(QCoreApplication.translate("ExpedienteDialog", u"<html><head/><body><p align=\"right\">Ingrese el nombre</p></body></html>", None))
    # retranslateUi

