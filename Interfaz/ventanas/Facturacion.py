from datetime import datetime
import json
import logging
import os
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QListWidget, QVBoxLayout, QListWidgetItem, QHBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap

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
    
    def to_dict(self):
        return {
            "nombre": self.descripcion,
            "precio_final": self.costo + (self.costo * self.iva / 100)
        }
    
class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Imagen")
        self.setGeometry(100, 100, 300, 300)  # Ajusta el tamaño según sea necesario

        layout = QVBoxLayout()
        
        self.label = QLabel(self)
        layout.addWidget(self.label)

        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio))
        self.label.setFixedSize(500, 500)
        self.label.setScaledContents(True)

        # Crear el botón
        self.button = QPushButton("Registrar Pago")
        self.button.setFixedSize(200, 50)
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_clicked(self):
        QMessageBox.information(self, "Pago Registrado", "El pago ha sido registrado")
        
class ProductoItem(QWidget):
    def __init__(self, producto, remove_callback):
        super().__init__()
        self.producto = producto
        self.remove_callback = remove_callback

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(self.producto.__str__())
        layout.addWidget(self.label)

        self.remove_button = QPushButton("X")
        self.remove_button.setFixedSize(20, 20)
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

    def remove_item(self):
        self.remove_callback(self.producto)
    
class ProductosListView(QWidget):
    def __init__(self, productos, remove_callback):
        super().__init__()
        self.setWindowTitle("Lista de Productos Seleccionados")
        self.setGeometry(100, 100, 600, 400)
        self.remove_callback = remove_callback

        layout = QVBoxLayout()

        self.list_view = QListWidget()
        layout.addWidget(self.list_view)

        self.total_label = QLabel("Total: $0.00")
        layout.addWidget(self.total_label)
        self.process_payment_button = QPushButton("Procesar el Pago")
        self.process_payment_button.clicked.connect(self.process_payment)
        layout.addWidget(self.process_payment_button)
        self.load_data(productos)
        self.setLayout(layout)
        self.update_total()

    def process_payment(self):
        self.procesar_window = ProcesarPagos(self.productos)
        self.procesar_window.payment_processed.connect(self.on_payment_processed)
        self.procesar_window.show()

    def on_payment_processed(self):
        self.productos.clear()
        self.load_data(self.productos)
        self.update_total()
        self.close()

    def load_data(self, productos):
        self.productos = productos
        self.list_view.clear()
        for producto in productos:
            item_widget = ProductoItem(producto, self.remove_product)
            list_item = QListWidgetItem(self.list_view)
            list_item.setSizeHint(item_widget.sizeHint())
            self.list_view.addItem(list_item)
            self.list_view.setItemWidget(list_item, item_widget)

    def update_total(self):
        total_amount = sum(producto.precio_final() for producto in self.productos)
        self.total_label.setText(f"Total: ${total_amount:.2f}")

    def remove_product(self, producto):
        self.productos.remove(producto)
        self.load_data(self.productos)
        self.update_total()

class ProcesarPagos(QWidget):
    payment_processed = pyqtSignal()

    def __init__(self, productos):
        super().__init__()
        uic.loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Pagos_Fisicos.ui", self)
        self.productos = productos
        self.update_total()
        self.pushButton.clicked.connect(self.procesar_pago)

    def update_total(self):
        total_amount = sum(producto.precio_final() for producto in self.productos)
        self.label_23.setText(f"${total_amount:.2f}")

    def procesar_pago(self):
        nombre_completo = self.lineEdit_2.text()

        if self.checkBox.isChecked():
            self.image_window = ImageWindow(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Imagenes\datafono.jpg")
            self.image_window.show()

        if self.checkBox_2.isChecked() or self.checkBox_3.isChecked() or self.checkBox_4.isChecked():
            print("procesado")

        now = datetime.now()
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        numero_transaccion = random.randint(1000000, 9999999)
        articulos_comprados = [producto.to_dict() for producto in self.productos]

        data = {
            "nombre": nombre_completo,
            "hora": fecha_hora,
            "numero_transaccion": numero_transaccion,
            "total": self.label_23.text(),
            "articulos_comprados": articulos_comprados
        }

        json_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Servicios_Fisicos.json"
        try:
            existing_data = []
            if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
                with open(json_path, "r", encoding='utf-8') as json_file:
                    existing_data = json.load(json_file)

            existing_data.append(data)

            with open(json_path, "w", encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, indent=4, ensure_ascii=False)

            self.show_message("Su pago fue procesado", "Pago Procesado")
            self.payment_processed.emit()
            self.close()
            
        except Exception as e:
            logging.error(f"Error while writing purchase data: {e}")

    def show_message(self, message, title):
        QMessageBox.information(self, title, message)   

class Facturacion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Facturación.ui", self)
        self.tableWidget.setColumnWidth(0, 280)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.productos = []
        self.tratamientos = []
        self.selected_products = []
        self.loaddata()
        self.loadtratamientos()
        self.pushButton.clicked.connect(self.show_selected_productos_list)
        
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

    def show_selected_productos_list(self):
        if self.selected_products:
            self.productos_list = ProductosListView(self.selected_products, self.remove_product_from_selected)
            self.productos_list.show()
        else:
            self.showWarningMessage("No hay productos seleccionados.")

    def remove_product_from_selected(self, producto):
        self.selected_products.remove(producto)

    def showWarningMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle("Sin Stock")
        msg_box.setStyleSheet("QLabel { color : white }")
        msg_box.exec()

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

    def handleButtonClicked(self, row):
        product = self.productos[row]
        self.selected_products.append(product)

