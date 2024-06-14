# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuscarMascota.ui'
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
        Dialog.resize(1404, 902)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 140, 191, 51))
        font = QFont()
        font.setFamilies([u"Bauhaus 93"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(77, 115, 129);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 280, 191, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 210, 191, 51))
        self.pushButton_3.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 97, 62);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 50, 691, 61))
        self.label_4.setStyleSheet(u"font: 25pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(22, 61, 76);\n"
"background-color: rgb(94, 140, 157);")
        self.lineEditNombreMascota = QLineEdit(Dialog)
        self.lineEditNombreMascota.setObjectName(u"lineEditNombreMascota")
        self.lineEditNombreMascota.setGeometry(QRect(720, 150, 481, 41))
        self.lineEditNombreMascota.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.lineEditNombreDueno = QLineEdit(Dialog)
        self.lineEditNombreDueno.setObjectName(u"lineEditNombreDueno")
        self.lineEditNombreDueno.setGeometry(QRect(720, 220, 481, 41))
        self.lineEditNombreDueno.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEditEspecie = QLineEdit(Dialog)
        self.lineEditEspecie.setObjectName(u"lineEditEspecie")
        self.lineEditEspecie.setGeometry(QRect(720, 290, 481, 41))
        self.lineEditEspecie.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButtonBuscar = QPushButton(Dialog)
        self.pushButtonBuscar.setObjectName(u"pushButtonBuscar")
        self.pushButtonBuscar.setGeometry(QRect(1240, 190, 151, 61))
        self.pushButtonBuscar.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"color: WHITE;\n"
"background-color: rgb(39, 39, 39);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 70, 251, 81))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 49pt \"Showcard Gothic\";")
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 160, 261, 5))
        self.line.setMaximumSize(QSize(16777215, 5))
        self.line.setStyleSheet(u"background-color: rgb(224, 123, 79);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 170, 271, 31))
        self.label_3.setStyleSheet(u"font: 20pt \"Forte\";\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 330, 171, 31))
        self.label_5.setStyleSheet(u"font: 25pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(224, 123, 79);\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1100, 40, 91, 81))
        self.label.setStyleSheet(u"background-color: rgb(94, 140, 157);")
        self.label.setPixmap(QPixmap(u"Imagenes/search_icon_125165.png"))
        self.label.setScaledContents(True)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(480, 40, 751, 311))
        self.frame_2.setStyleSheet(u"background-color: rgb(94, 140, 157);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 380, 1201, 511))
        self.frame_3.setStyleSheet(u"background-color: rgb(94, 140, 157);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 1161, 461))
        self.frame.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidgetResultados = QTableWidget(self.frame)
        self.tableWidgetResultados.setObjectName(u"tableWidgetResultados")
        self.tableWidgetResultados.setGeometry(QRect(10, 10, 1141, 441))
        self.tableWidgetResultados.setAutoFillBackground(False)
        self.tableWidgetResultados.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe MDL2 Assets\";")
        self.tableWidgetResultados.setFrameShape(QFrame.WinPanel)
        self.tableWidgetResultados.setLineWidth(8)
        self.tableWidgetResultados.setMidLineWidth(4)
        self.tableWidgetResultados.setAlternatingRowColors(False)
        self.tableWidgetResultados.setWordWrap(True)
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1250, 830, 141, 61))
        self.pushButton_4.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"color: WHITE;\n"
"background-color: rgb(39, 39, 39);")
        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 230, 301, 5))
        self.line_2.setMaximumSize(QSize(16777215, 5))
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(Dialog)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(30, 60, 5, 171))
        self.line_8.setMaximumSize(QSize(5, 16777215))
        self.line_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_9 = QFrame(Dialog)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(330, 60, 5, 171))
        self.line_9.setMaximumSize(QSize(5, 16777215))
        self.line_9.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 60, 301, 5))
        self.line_3.setMaximumSize(QSize(16777215, 5))
        self.line_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 350, 1411, 21))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"Segoe UI\";")
        self.frame_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_4.raise_()
        self.lineEditNombreMascota.raise_()
        self.lineEditNombreDueno.raise_()
        self.lineEditEspecie.raise_()
        self.pushButtonBuscar.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.frame_3.raise_()
        self.pushButton_4.raise_()
        self.line_2.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_3.raise_()
        self.label_6.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Nombre Mascota:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Especie:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Nombre Due\u00f1o:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Buscar mascota por Nombre, Due\u00f1o o Especie", None))
        self.pushButtonBuscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"MI PET", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Busqueda de Clientes", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"RESULTADOS:", None))
        self.label.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u". . . . . . . . . .  . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ", None))
    # retranslateUi

