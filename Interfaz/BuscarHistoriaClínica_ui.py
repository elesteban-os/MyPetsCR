# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuscarHistoriaClínica.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1229, 773)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 140, 271, 31))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 26pt \"Tw Cen MT Condensed Extra Bold\";")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(720, 60, 101, 21))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(850, 60, 161, 21))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 160, 541, 51))
        self.label_11.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(940, 170, 131, 41))
        font1 = QFont()
        font1.setFamilies([u"Bauhaus 93"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"background-color: rgb(255, 191, 146);")
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(550, 170, 351, 41))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 230, 491, 41))
        self.label_12.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit_7 = QTextEdit(self.centralwidget)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(550, 240, 351, 41))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(940, 240, 131, 41))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Bauhaus 93\";\n"
"background-color: rgb(255, 191, 146);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 50, 231, 41))
        self.label_4.setStyleSheet(u"font: 27pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(224, 123, 79);\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 321, 20))
        self.label_3.setStyleSheet(u"font: 17pt \"Forte\";\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 231, 81))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 49pt \"Showcard Gothic\";")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 90, 241, 5))
        self.line.setMaximumSize(QSize(16777215, 5))
        self.line.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 310, 1191, 441))
        self.frame.setStyleSheet(u"background-color: rgb(224, 123, 79);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 1171, 421))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe MDL2 Assets\";")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 290, 1231, 5))
        self.line_2.setMaximumSize(QSize(16777215, 5))
        self.line_2.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Mascota ", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Datos del Due\u00f1o", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Digite el nombre de la mascota a la cual desea consultar el historial cl\u00ednico: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Digite el nombre del due\u00f1o para buscar el expediente de la mascota: ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Buscar ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Consultar por : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Consultas del Historial Cl\u00ednico", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MI PET", None))
    # retranslateUi

