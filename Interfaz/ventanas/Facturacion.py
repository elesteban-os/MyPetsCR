import json
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton
from PyQt6 import uic

class Producto:
    def __init__(self, Código, Descripción, Costo, IVA):
        self.codigo = Código
        self.descripcion = Descripción
        self.iva = IVA
        self.costo = Costo

    def precio_final(self):
        return self.costo + (self.costo * self.iva / 100)

    def __str__(self):
        return f"{self.descripcion} - ${self.precio_final():.2f}"

class Facturacion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Facturación.ui", self)
        self.tableWidget.setColumnWidth(0, 280)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.productos = []
        self.tratamientos = []
        self.loaddata()
        self.loadtratamientos()
        
    #cargo los tratamientos que el veterinario puso
    def loadtratamientos(self):
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\ventanas\Tratamientos_Vete.json"

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if "servicios" in data and isinstance(data["servicios"], list):
                    self.tratamientos = data["servicios"]
                    for tratamiento in self.tratamientos:
                        item = QtWidgets.QListWidgetItem(tratamiento)
                        self.listWidget.addItem(item)
                else:
                    print("La clave 'servicios' no existe o no es una lista en el JSON")
        else:
            print(f"El archivo {json_file_path} no existe")


    #cargo los servicios que la veterinaria brinda
    def loaddata(self):
        #esto agarra las cosas del archivo json
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Servicios.json"

        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    producto = Producto(**item)
                    self.productos.append(producto)
        else:
            raise FileNotFoundError(f"The file {json_file_path} does notexist.")
        self.tableWidget.setRowCount(len(self.productos))

        for row, producto in enumerate(self.productos):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(producto.descripcion))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{producto.precio_final():.2f}"))
            
            button = QPushButton("Agregar")
            button.clicked.connect(lambda checked, r=row: self.handleButtonClicked(r))
            self.tableWidget.setCellWidget(row, 2, button)


