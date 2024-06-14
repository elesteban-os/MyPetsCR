# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tienda.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1119, 656)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 50, 101, 41))
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
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(510, 50, 101, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(650, 50, 161, 41))
        self.pushButton_3.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 97, 62);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 230, 801, 401))
        self.frame.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(0, 170, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 781, 381))
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
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 331, 141))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 311, 91))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 38pt \"Showcard Gothic\";")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 141, 101))
        self.label_2.setPixmap(QPixmap(u"Imagenes/mipet2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 110, 151, 20))
        self.label_3.setStyleSheet(u"font: 14pt \"Forte\";\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 190, 141, 31))
        self.label_4.setStyleSheet(u"font: 25pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, 160, 1131, 16))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(850, 340, 221, 221))
        self.frame_4.setStyleSheet(u"background-color: rgb(177, 97, 62);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1080, 20, 31, 31))
        self.label_7.setStyleSheet(u"font: 900 15pt \"Segoe UI Black\";\n"
"color: rgb(0, 188, 0);")
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(940, 30, 61, 61))
        self.pushButton_4.setMinimumSize(QSize(31, 31))
        self.pushButton_4.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"Imagenes/OIP.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(55, 55))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1020, 40, 61, 51))
        self.pushButton_5.setMinimumSize(QSize(31, 31))
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/shopping_cart_PNG38.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(55, 55))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 635, 451, 21))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Showcard Gothic\";")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(820, 310, 301, 21))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Tw Cen MT Condensed Extra Bold\";")
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(600, 190, 201, 31))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 72, 91);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(255, 0, 0);\n"
"border-radius: 20;")

        self.retranslateUi(Form)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Inicio", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Contacto", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Agendar una cita", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Marca", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Disponible", None));
        self.label.setText(QCoreApplication.translate("Form", u"MI              PET", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"tienda en linea", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ARTICULOS", None))
        self.label_7.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Todos los articulos incluyen el impuesto de venta (IVA)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"para ver la imagen del articulo dale click al mismo!!", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Historial de Compras", None))
    # retranslateUi

