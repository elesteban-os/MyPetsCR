# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistorialClinico_Cliente.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1311, 975)
        self.actionhola = QAction(MainWindow)
        self.actionhola.setObjectName(u"actionhola")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 381, 91))
        self.label_4.setStyleSheet(u"font: 25pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 80, 261, 21))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 13pt \"Tw Cen MT Condensed Extra Bold\";")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(610, 80, 251, 21))
        self.radioButton_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 120, 131, 51))
        font = QFont()
        font.setFamilies([u"Bauhaus 93"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 351, 61))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 210, 601, 331))
        self.frame.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 211, 51))
        self.label_2.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 97, 62);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 301, 61))
        self.label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 301, 61))
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 170, 301, 61))
        self.label_7.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 220, 301, 61))
        self.label_8.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 70, 331, 41))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(110, 180, 331, 41))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(110, 230, 251, 41))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 120, 221, 41))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 270, 301, 61))
        self.label_10.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.textEdit_6 = QTextEdit(self.frame)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(140, 280, 251, 41))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.comboBox.raise_()
        self.textEdit_3.raise_()
        self.label_10.raise_()
        self.textEdit_6.raise_()
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(640, 200, 771, 261))
        self.frame_2.setStyleSheet(u"background-color: rgb(26, 72, 91);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(230, 0, 191, 41))
        self.label_40.setStyleSheet(u"font: 14pt \"Bauhaus 93\";\n"
"border-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 97, 62);")
        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 50, 91, 61))
        self.label_41.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 120, 301, 61))
        self.label_43.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 180, 301, 61))
        self.label_44.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(390, 60, 301, 61))
        self.label_49.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.label_45 = QLabel(self.frame_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(400, 180, 301, 61))
        self.label_45.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.textEdit_4 = QTextEdit(self.frame_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(120, 70, 261, 41))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_5 = QTextEdit(self.frame_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(480, 70, 271, 41))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_7 = QTextEdit(self.frame_2)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(110, 140, 261, 41))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_8 = QTextEdit(self.frame_2)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(110, 200, 261, 41))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit_9 = QTextEdit(self.frame_2)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(470, 200, 261, 41))
        self.textEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 560, 301, 51))
        self.label_11.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(370, 560, 211, 61))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 640, 581, 271))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe MDL2 Assets\";")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(860, 510, 301, 51))
        self.label_12.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.rowCount() < 9):
            self.tableWidget_2.setRowCount(9)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(690, 580, 581, 321))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe MDL2 Assets\";")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1100, 30, 381, 91))
        self.label_13.setStyleSheet(u"font: 25pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color: rgb(26, 72, 91);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionhola.setText(QCoreApplication.translate("MainWindow", u"hola", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Historia Cl\u00ednica ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Seeleccione lo que desea hacer: ", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar Historia Cl\u00ednica", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seleccione la historia Cl\u00ednica:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Datos del Paciente: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Especie: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Raza: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Edad: ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ID Due\u00f1o: ", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Datos del Due\u00f1o: ", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Telefono: ", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n: ", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"email: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Veterinario que lo est\u00e1 tratando: ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Consultas ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Desparasitaci\u00f3n", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Vacunas ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cirug\u00edas ", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Historia Cl\u00ednica: ", None))
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Alergias:", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"S\u00edntomas: ", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Enfermedades que padece: ", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Anomalidades:", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3stico previo:", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Diagn\u00f3tico Final: ", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Tratamiento: ", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Estado en general: ", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Comentarios: ", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Vista Cliente", None))
    # retranslateUi

