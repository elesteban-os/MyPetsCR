# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana0.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 755)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 291, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 170, 127);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 120, 451, 71))
        self.label_2.setStyleSheet(u"color:white;\n"
"font: 30pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 250, 311, 71))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 199, 167);\n"
"border-radius:20px;\n"
"color: ;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(490, 340, 311, 61))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(255, 199, 167);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: black;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 210, 321, 201))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(510, 630, 321, 51))
        self.pushButton_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 10, 281, 91))
        self.label_3.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;\n"
"border-radius:20px;\n"
"background-color:rgb(255, 170, 127);\n"
"")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(340, 380, 118, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(340, 280, 118, 3))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(460, 230, 371, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 869, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">MiPet</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Elige tu opci\u00f3n </span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n MiPet", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tienda en L\u00ednea", None))
        self.label_6.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Inicio</span></p></body></html>", None))
    # retranslateUi

