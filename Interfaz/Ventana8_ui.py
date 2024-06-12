# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana8.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMdiArea,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import Imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1115, 803)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255))};\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 0, 561, 101))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-40, 0, 181, 111))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 160, 361, 41))
        self.pushButton_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 430, 221, 51))
        self.pushButton_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(870, 700, 251, 51))
        self.pushButton_5.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: red;")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(160, 280, 321, 51))
        self.pushButton_6.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(160, 550, 441, 41))
        self.pushButton_7.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 121, 111))
        self.label_3.setStyleSheet(u"image: url(:/login/Imagen3.png)")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-70, 190, 391, 261))
        self.label_5.setStyleSheet(u"image: url(:/login/Imagen 6.png)\n"
"\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 510, 121, 111))
        self.label_8.setStyleSheet(u"image:  url(:/login/Imagen1.png)")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 390, 161, 101))
        self.label_10.setStyleSheet(u"image: url(:/login/Imagen8.png)")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 80, 551, 51))
        self.mdiArea_4 = QMdiArea(self.centralwidget)
        self.mdiArea_4.setObjectName(u"mdiArea_4")
        self.mdiArea_4.setGeometry(QRect(160, 140, 351, 71))
        self.mdiArea_5 = QMdiArea(self.centralwidget)
        self.mdiArea_5.setObjectName(u"mdiArea_5")
        self.mdiArea_5.setGeometry(QRect(190, 270, 311, 71))
        self.mdiArea_6 = QMdiArea(self.centralwidget)
        self.mdiArea_6.setObjectName(u"mdiArea_6")
        self.mdiArea_6.setGeometry(QRect(190, 420, 221, 71))
        self.mdiArea_7 = QMdiArea(self.centralwidget)
        self.mdiArea_7.setObjectName(u"mdiArea_7")
        self.mdiArea_7.setGeometry(QRect(220, 540, 411, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.mdiArea_7.raise_()
        self.mdiArea_6.raise_()
        self.mdiArea_5.raise_()
        self.mdiArea_4.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Veterinaria MiPet", None))
        self.label_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Historial Cl\u00ednico del Paciente", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Citas Proximas", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Expediente de Mascotas", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u" Registro de Servicios prestados", None))
        self.label_3.setText("")
        self.label_5.setText("")
        self.label_8.setText("")
        self.label_10.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffaa7f;\">Bienvenido Veterinari@!</span></p></body></html>", None))
    # retranslateUi

