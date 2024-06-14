# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuscarCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1204, 790)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 251, 111))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 49pt \"Showcard Gothic\";")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 340, 1121, 421))
        self.frame.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 1101, 401))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe MDL2 Assets\";")
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setLineWidth(8)
        self.tableWidget.setMidLineWidth(4)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setWordWrap(True)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 280, 421, 31))
        self.label_4.setStyleSheet(u"font: 29pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(850, 210, 201, 51))
        font = QFont()
        font.setFamilies([u"Bauhaus 93"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 72, 91);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(255, 0, 0);\n"
"border-radius: 20;")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(730, 140, 451, 51))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 150, 131, 31))
        self.label_5.setStyleSheet(u"font: 29pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: Black;\n"
"")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(510, 40, 681, 81))
        self.label_6.setStyleSheet(u"font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(224, 123, 79);\n"
"")
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 130, 261, 5))
        self.line.setMaximumSize(QSize(16777215, 5))
        self.line.setStyleSheet(u"background-color: rgb(224, 123, 79);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 331, 51))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 20pt \"Showcard Gothic\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"MI PET", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Resultados de Busqueda: ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Buscar ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Cliente:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>A\u00f1ade el nombre a quien quieres asignar de due\u00f1o de la mascota</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"busqueda por cliente", None))
    # retranslateUi

