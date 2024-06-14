# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistorialVet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_ExpedienteDialog(object):
    def setupUi(self, ExpedienteDialog):
        if not ExpedienteDialog.objectName():
            ExpedienteDialog.setObjectName(u"ExpedienteDialog")
        ExpedienteDialog.resize(1291, 883)
        ExpedienteDialog.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.239, y1:0.295455, x2:1, y2:1, stop:0.308458 rgba(26, 72, 91, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(ExpedienteDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(-10, 20, 1301, 681))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 0, 281, 91))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color:red;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(780, 610, 221, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(224, 123, 79);\n"
"border-radius:20px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1040, 610, 151, 51))
        self.pushButton_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(224, 123, 79);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-70, -10, 261, 131))
        self.label_6.setStyleSheet(u"image: url(:/login/Imagen2.jpg)")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 120, 851, 81))
        self.label_7.setStyleSheet(u"color:white;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 11):
            self.tableWidget.setRowCount(11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(150, 200, 1000, 350))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(320)
        self.menubar = QMenuBar(ExpedienteDialog)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1291, 26))
        self.statusbar = QStatusBar(ExpedienteDialog)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 21))

        self.retranslateUi(ExpedienteDialog)

        QMetaObject.connectSlotsByName(ExpedienteDialog)
    # setupUi

    def retranslateUi(self, ExpedienteDialog):
        ExpedienteDialog.setWindowTitle(QCoreApplication.translate("ExpedienteDialog", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ExpedienteDialog", u"MiPet", None))
        self.pushButton.setText(QCoreApplication.translate("ExpedienteDialog", u"Guardar Cambios ", None))
        self.pushButton_2.setText(QCoreApplication.translate("ExpedienteDialog", u"Cancelar ", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("ExpedienteDialog", u"Historial Cl\u00ednico", None))
        self.tableWidget.setProperty("horizontalHeaderLabels", [
            QCoreApplication.translate("ExpedienteDialog", u"Fecha", None),
            QCoreApplication.translate("ExpedienteDialog", u"Descripci\u00f3n", None),
            QCoreApplication.translate("ExpedienteDialog", u"Doctor", None)])
    # retranslateUi

