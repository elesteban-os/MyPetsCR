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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 688)
        MainWindow.setStyleSheet(u"background-color: rgb(224, 123, 79);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 80, 1151, 631))
        self.frame.setTabletTracking(True)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1100, 10, 41, 41))
        self.pushButton_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"color: white;\n"
"background-color: rgb(77, 115, 129);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 30, 371, 131))
        self.label.setStyleSheet(u"font: 80pt \"Showcard Gothic\";\n"
"color: rgb(26, 72, 91);")
        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(650, 190, 118, 3))
        self.line_7.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(390, 190, 118, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(650, 30, 118, 3))
        self.line_8.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(390, 30, 118, 3))
        self.line_4.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 150, 191, 20))
        self.label_2.setStyleSheet(u"font: 17pt \"Forte\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(800, 290, 221, 61))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(77, 115, 129);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 300, 221, 61))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(77, 115, 129);\n"
"border-radius:20px;\n"
"color: white ;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 270, 311, 251))
        self.label_3.setPixmap(QPixmap(u"Imagenes/mipet2.jpg"))
        self.label_3.setScaledContents(True)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(120, 90, 101, 16))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(120, 110, 101, 16))
        self.frame_3.setStyleSheet(u"background-color: rgb(195, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(120, 130, 101, 16))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(370, 40, 3, 61))
        self.line_5.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_51 = QFrame(self.frame)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setGeometry(QRect(520, 190, 118, 3))
        self.line_51.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_51.setFrameShape(QFrame.Shape.HLine)
        self.line_51.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_52 = QFrame(self.frame)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setGeometry(QRect(520, 30, 118, 3))
        self.line_52.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_52.setFrameShape(QFrame.Shape.HLine)
        self.line_52.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_53 = QFrame(self.frame)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setGeometry(QRect(370, 110, 3, 61))
        self.line_53.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_53.setFrameShape(QFrame.Shape.VLine)
        self.line_53.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_54 = QFrame(self.frame)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setGeometry(QRect(780, 110, 3, 61))
        self.line_54.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_54.setFrameShape(QFrame.Shape.VLine)
        self.line_54.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(950, 90, 101, 16))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(950, 110, 101, 16))
        self.frame_6.setStyleSheet(u"background-color: rgb(195, 0, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(950, 130, 101, 16))
        self.frame_7.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 230, 841, 31))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(True)
        self.label_4.setStyleSheet(u"font: 11pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.line_9 = QFrame(self.frame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(780, 40, 3, 61))
        self.line_9.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 450, 221, 61))
        self.pushButton_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(77, 115, 129);\n"
"border-radius:20px;\n"
"color: white ;")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(810, 430, 211, 61))
        self.pushButton_5.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(77, 115, 129);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(20, 10, 1131, 61))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 291, 31))
        self.label_5.setFont(font)
        self.label_5.setAcceptDrops(True)
        self.label_5.setStyleSheet(u"font: 11pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);")
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1070, 10, 41, 41))
        self.pushButton_6.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"color: white;\n"
"background-color: rgb(77, 115, 129);")
        icon = QIcon()
        icon.addFile(u"Imagenes/facebook2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1020, 10, 41, 41))
        self.pushButton_7.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"color: white;\n"
"background-color: rgb(77, 115, 129);")
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/insta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(24, 24))
        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(970, 10, 41, 41))
        self.pushButton_8.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"border-radius:20px;\n"
"color: white;\n"
"background-color: rgb(77, 115, 129);")
        icon2 = QIcon()
        icon2.addFile(u"Imagenes/tiktok-share-icon-black-logo-29FFD062A0-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mi Pet", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Clinica Veterinaria", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tienda en L\u00ednea", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n MiPet", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Brindamos con calidad humana y profesionalismo la mejor atenci\u00f3n a nuestros pacientes y sus propietarios", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Contacto", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Nuestras Tiendas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lunes-S\u00e1bado: 7:00 hrs a 20:30 hrs", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
    # retranslateUi

