# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaMostrarDatos.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1298, 811)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidgetClientes = QTableWidget(self.centralwidget)
        self.tableWidgetClientes.setObjectName(u"tableWidgetClientes")
        self.tableWidgetClientes.setGeometry(QRect(10, 90, 621, 511))
        self.pushButtonCerrar = QPushButton(self.centralwidget)
        self.pushButtonCerrar.setObjectName(u"pushButtonCerrar")
        self.pushButtonCerrar.setGeometry(QRect(1050, 720, 231, 51))
        self.pushButtonCerrar.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.tableWidgetPersonas = QTableWidget(self.centralwidget)
        self.tableWidgetPersonas.setObjectName(u"tableWidgetPersonas")
        self.tableWidgetPersonas.setGeometry(QRect(640, 90, 651, 511))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 401, 31))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(700, 30, 541, 41))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color:white;")
        self.pushButtonLimpiarClientes = QPushButton(self.centralwidget)
        self.pushButtonLimpiarClientes.setObjectName(u"pushButtonLimpiarClientes")
        self.pushButtonLimpiarClientes.setGeometry(QRect(10, 620, 291, 51))
        self.pushButtonLimpiarClientes.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButtonLimpiarPersonas = QPushButton(self.centralwidget)
        self.pushButtonLimpiarPersonas.setObjectName(u"pushButtonLimpiarPersonas")
        self.pushButtonLimpiarPersonas.setGeometry(QRect(640, 620, 291, 51))
        self.pushButtonLimpiarPersonas.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonCerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datos de Clientes ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Datos de Administradores y Veterinarios", None))
        self.pushButtonLimpiarClientes.setText(QCoreApplication.translate("MainWindow", u"Limpiar Clientes ", None))
        self.pushButtonLimpiarPersonas.setText(QCoreApplication.translate("MainWindow", u"Limpiar Personal", None))
    # retranslateUi

