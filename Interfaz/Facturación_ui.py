# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Facturación.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(939, 686)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(580, 30, 341, 311))
        self.frame.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 331, 31))
        self.label_5.setStyleSheet(u"font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 321, 251))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 80, 551, 551))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 500, 121, 41))
        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 60, 531, 421))
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
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 211, 31))
        self.label_4.setStyleSheet(u"font: 22pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 640, 551, 41))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Showcard Gothic\";")
        self.label_6.setWordWrap(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 391, 61))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 30pt \"Showcard Gothic\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tratamiento por Veterinario", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Tramitar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Costo", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"A\u00f1adir servicios", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Todos los servicios se deben tramitar por sesi\u00f3n incluyendo el impuesto de venta(IVA)", None))
        self.label.setText(QCoreApplication.translate("Form", u"Facturaci\u00f3n", None))
    # retranslateUi

