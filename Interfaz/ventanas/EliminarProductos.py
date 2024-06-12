import json
import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem

class Producto:
    def __init__(self, Código, Descripción, Marca, Precio, IVA, CantidadDisponible, Categoría, Imagen):
        self.codigo = Código
        self.descripcion = Descripción
        self.marca = Marca
        self.precio = Precio
        self.iva = IVA
        self.cantidad_disponible = CantidadDisponible
        self.categoria = Categoría
        self.imagen = Imagen

    def precio_final(self):
        return self.precio + (self.precio * self.iva / 100)

    def __str__(self):
        return f"{self.descripcion} ({self.marca}) - ${self.precio_final():.2f}"

class EliminarProductos(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\BorrarArticulos.ui", self)
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.productos = []  # Inicializar la lista de productos
        self.json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Productos_Veterinaria (1).json"
        self.loaddata()

    def loaddata(self):
        # Esto carga los productos desde el archivo JSON
        if os.path.isfile(self.json_file_path):
            with open(self.json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    producto = Producto(**item)
                    self.productos.append(producto)
        else:
            raise FileNotFoundError(f"The file {self.json_file_path} does not exist.")
        
        self.tableWidget.setRowCount(len(self.productos))

        for row, producto in enumerate(self.productos):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(producto.descripcion))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(producto.marca))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{producto.precio_final():.2f}"))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(producto.cantidad_disponible)))
            # Botón para eliminar
            button = QPushButton("Eliminar")
            button.clicked.connect(lambda checked, r=row: self.handleButtonClicked(r))
            self.tableWidget.setCellWidget(row, 4, button)

    def handleButtonClicked(self, row):
        # Elimina el producto de la lista
        del self.productos[row]
        # Actualiza el archivo JSON
        self.update_json_file()
        # Actualiza la tabla
        self.tableWidget.removeRow(row)

    def update_json_file(self):
        # Convierte los objetos Producto a diccionarios con la estructura original
        data = [{
            "Código": producto.codigo,
            "Descripción": producto.descripcion,
            "Marca": producto.marca,
            "Precio": producto.precio,
            "IVA": producto.iva,
            "CantidadDisponible": producto.cantidad_disponible,
            "Categoría": producto.categoria,
            "Imagen": producto.imagen
        } for producto in self.productos]

        # Guarda los productos actualizados en el archivo JSON
        with open(self.json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EliminarProductos()
    window.show()
    sys.exit(app.exec())
