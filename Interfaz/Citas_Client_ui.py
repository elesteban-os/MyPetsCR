# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Citas_Client.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(123, 168, 198, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(112, 147, 199, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 371, 71))
        palette1 = QPalette()
        brush2 = QBrush(QColor(253, 253, 253, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(18)
        font.setBold(False)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 241, 71))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label_2.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.sede = QComboBox(self.centralwidget)
        self.sede.setObjectName(u"sede")
        self.sede.setGeometry(QRect(50, 150, 251, 41))
        palette3 = QPalette()
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(9, 9, 9, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush6)
        brush7 = QBrush(QColor(4, 6, 7, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        brush8 = QBrush(QColor(81, 151, 184, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush8)
        brush9 = QBrush(QColor(2, 2, 2, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush9)
        brush10 = QBrush(QColor(159, 195, 198, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        brush11 = QBrush(QColor(127, 184, 178, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.NoRole, brush11)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.NoRole, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        brush12 = QBrush(QColor(88, 191, 211, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.NoRole, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        self.sede.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(9)
        self.sede.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 220, 241, 71))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label_3.setPalette(palette4)
        self.label_3.setFont(font1)
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(450, 290, 271, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        self.dateTimeEdit.setPalette(palette5)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 270, 241, 71))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.label_4.setPalette(palette6)
        self.label_4.setFont(font1)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 340, 291, 131))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.textEdit.setPalette(palette7)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 360, 251, 51))
        palette8 = QPalette()
        brush13 = QBrush(QColor(120, 173, 202, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        self.pushButton_2.setPalette(palette8)
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_2.setFont(font3)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 430, 131, 41))
        self.pushButton.setFont(font3)
        self.nombrecliente = QLabel(self.centralwidget)
        self.nombrecliente.setObjectName(u"nombrecliente")
        self.nombrecliente.setGeometry(QRect(50, 190, 241, 71))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.nombrecliente.setPalette(palette9)
        self.nombrecliente.setFont(font1)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 250, 281, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette10.setBrush(QPalette.Active, QPalette.NoRole, brush10)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.NoRole, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.NoRole, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        self.lineEdit.setPalette(palette10)
        self.correo = QLabel(self.centralwidget)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(430, 110, 291, 71))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.correo.setPalette(palette11)
        self.correo.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(430, 180, 281, 31))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Active, QPalette.NoRole, brush10)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.NoRole, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.NoRole, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        self.lineEdit_2.setPalette(palette12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reservaci\u00f3n de citas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccionar sede:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Horario disponible", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Motivo de la cita:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Enviar confirmaci\u00f3n", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.nombrecliente.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.correo.setText(QCoreApplication.translate("MainWindow", u"Correo de confirmaci\u00f3n:", None))
    # retranslateUi
