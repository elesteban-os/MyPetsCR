import os
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import QtWidgets, QtGui
from PyQt6 import uic
from PyQt6.QtGui import QColor
import sys

class Pagos(QtWidgets.QWidget):
    def __init__(self, selected_products):
        super().__init__()
        ui_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Pagos.ui"
        if not os.path.isfile(ui_file_path):
            raise FileNotFoundError(f"The file {ui_file_path} does not exist.")
        uic.loadUi(ui_file_path, self)
        self.selected_products = selected_products
        print(f"Processing payment for: {self.selected_products}")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selected_products = ["Example Product"]  # Example data
    window = Pagos(selected_products)
    window.show()
    sys.exit(app.exec())