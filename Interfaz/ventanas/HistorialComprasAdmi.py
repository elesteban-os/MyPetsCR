import sys
import json
from PyQt6 import QtWidgets, uic

class HistorialComprasAdmi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\HistorialdeFacturacionesCliente.ui", self)
        self.setup_ui()

    def setup_ui(self):
        # Acceder al widget de la tabla
        self.table_widget = self.findChild(QtWidgets.QTableWidget, 'tableWidget_2')
        self.cargar_historial()

    def cargar_historial(self):
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\ComprasClientes.json"
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                datos_compras = json.load(file)
        except FileNotFoundError:
            datos_compras = []
            print(f"No se encontró el archivo: {json_file_path}")

        # Limpiar filas existentes
        self.table_widget.setRowCount(0)

        # Cargar datos en la tabla
        for transaccion in datos_compras:
            if 'articulos_comprados' not in transaccion:
                print(f"Transacción sin 'articulos_comprados': {transaccion}")
                continue
            for articulo in transaccion['articulos_comprados']:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(transaccion['numero_transaccion'])))
                self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(transaccion['hora']))
                self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(transaccion['nombre']))
                self.table_widget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(articulo['nombre']))
                self.table_widget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(articulo['precio_final'])))
                self.table_widget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(transaccion.get('total', 'N/A'))))
                # Asumimos que no hay descuentos y el estado por defecto
                self.table_widget.setItem(row_position, 6, QtWidgets.QTableWidgetItem("0"))
                self.table_widget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(str(transaccion.get('total', 'N/A'))))
                self.table_widget.setItem(row_position, 8, QtWidgets.QTableWidgetItem("Completado"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = HistorialComprasAdmi()
    window.show()
    sys.exit(app.exec())