# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pagos_Fisicos.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(465, 525)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 441, 491))
        self.frame.setStyleSheet(u"background-color: rgb(197, 198, 199);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 90, 281, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 181, 16))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 271, 31))
        self.label_5.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 290, 401, 101))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 81, 31))
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(260, 20, 121, 20))
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 410, 141, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 150, 121, 16))
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_17.setWordWrap(True)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 180, 78, 22))
        self.checkBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(40, 230, 81, 22))
        self.checkBox_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(230, 180, 78, 22))
        self.checkBox_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(230, 230, 101, 22))
        self.checkBox_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre Completo", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Pago ", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"TOTAL:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Finalizar Transacci\u00f3n", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Metodo de Pago:", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Tarjeta", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Efectivo", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Sinpe", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Transferencia", None))
    # retranslateUi

