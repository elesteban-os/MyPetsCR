import json
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class HistorialCompras(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\HistorialdeFacturacionesVeterinaria.ui", self)
        self.cargar_historial()

    def cargar_historial(self):
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Servicios_Fisicos.json"
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        self.tableWidget_2.setRowCount(len(data))
        for row, compra in enumerate(data):
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(compra['numero_transaccion'])))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(compra['hora']))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(compra['nombre']))
            # Extraer los nombres de los artículos comprados
            articulos_comprados = ', '.join([articulo['nombre'] for articulo in compra['articulos_comprados']])
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(articulos_comprados))
            # Calcular el total de los precios de los artículos comprados
            total_precio_articulos = sum(articulo['precio_final'] for articulo in compra['articulos_comprados'])
            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_precio_articulos)))
            self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(compra['total']))

    def actualizar_historial(self, nueva_compra):
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Servicios_Fisicos.json"
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



