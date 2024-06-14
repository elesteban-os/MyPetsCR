import json
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class HistorialCompras(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\HistorialdeFacturacionesVeterinaria.ui", self)
        self.cargar_historial()

    def cargar_historial(self):
        json_file_path = r"C:\Users\Meibel\Downloads\MyPetsCR-main (1)\MyPetsCR-main\Interfaz\Historial_Compras.json"
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        self.tableWidget_2.setRowCount(len(data))
        for row, compra in enumerate(data):
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(compra['#Factura']))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(compra['Fecha']))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(compra['Cliente']))
            # Extraer los códigos de los productos comprados
            productos_comprados = ', '.join([producto['Código'] for producto in compra['Productos Comprados']])
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(productos_comprados))
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(sum(producto['Cantidad'] for producto in compra['Productos Comprados']))))
            self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(str(compra['Subtotal'])))
            self.tableWidget_2.setItem(row, 6, QtWidgets.QTableWidgetItem(str(compra['Descuento'])))
            self.tableWidget_2.setItem(row, 7, QtWidgets.QTableWidgetItem(str(compra['Total'])))
            self.tableWidget_2.setItem(row, 8, QtWidgets.QTableWidgetItem(compra['Estado']))

    def actualizar_historial(self, nueva_compra):
        json_file_path = r"C:\Users\Meibel\Downloads\MyPetsCR-main (1)\MyPetsCR-main\Interfaz\Historial_Compras.json"
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(nueva_compra)
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        self.cargar_historial()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = HistorialCompras()
    window.show()
    sys.exit(app.exec())



