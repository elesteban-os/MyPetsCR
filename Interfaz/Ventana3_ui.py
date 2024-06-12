# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana3.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 803)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: rgb(158, 110, 200)}")
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 520, 151, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 0, 255);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(770, 520, 151, 51))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(170, 0, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 30, 331, 201))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 290, 451, 91))
        self.label_3.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";\n"
"color:white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1053, 26))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salir ", None))
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00a1Ha ingresado correctamente!", None))
    # retranslateUi

