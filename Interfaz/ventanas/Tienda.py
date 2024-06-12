
import logging
import random
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QListWidget, QVBoxLayout, QListWidgetItem, QHBoxLayout, QDialog
from .HistorialCompras import HistorialCompras
from datetime import datetime
from .Login import Login
import os
import json

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
    
    def to_dict(self):
        return {
            "nombre": self.descripcion,
            "precio_final": self.precio + (self.precio * self.iva / 100)
        }

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

#aquí es donde tengo que agregar varas
    def process_payment(self):
        self.procesar_window = ProcesarPagos(self.productos)
        self.procesar_window.show()

class MetodosPagoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\MetodosPago.ui", self)

#esta clase es para procesar los pagos que se realizan
class ProcesarPagos(QWidget):
    def __init__(self, productos):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\ProcesarPagos.ui", self)
        self.productos = productos
        self.update_subtotal()
        self.pushButton.clicked.connect(self.tarjeta_selection)
        self.checkBox.stateChanged.connect(self.on_checkbox_state_changed)
        self.pushButton_2.clicked.connect(self.otros_metodos)
    def update_subtotal(self):
        subtotal_amount = sum(producto.precio_final() for producto in self.productos)
        self.label_19.setText(f"₡{subtotal_amount:.2f}")

    def update_total(self):
        subtotal_text = self.label_19.text().replace("₡", "")
        subtotal_amount = float(subtotal_text)
        total_amount = subtotal_amount + 4500  # Sumar el monto de envío
        self.label_23.setText(f"Total: ₡{total_amount:.2f}")

    def otros_metodos(self):
        metodos_pago_widget = MetodosPagoWidget(self)
        metodos_pago_widget.show()

    def on_checkbox_state_changed(self):
        if self.checkBox.isChecked():
            self.label_21.setText("₡4500")
            self.update_total()

        else:
            self.label_23.setText(self.label_19.text())
            self.label_21.setText("₡0")

    def validar_numero_tarjeta(numero):
        try:
            int(numero)  # Intenta convertir el valor a entero
            return True
        except ValueError:
            return False

    def tarjeta_selection(self):
        nombre = self.lineEdit_2.text()
        numeroDtarjeta = self.lineEdit.text()

        # Validar el número de tarjeta
        if not ProcesarPagos.validar_numero_tarjeta(numeroDtarjeta):
            QMessageBox.information(self, "Error", "Verifique bien sus datos")
            return  # Salir de la función si la validación falla
        vencimiento_tarjeta = self.comboBox.currentText() + "/" + self.comboBox_2.currentText()
        correo = self.lineEdit_4.text()
        ccv = self.lineEdit_3.text()
        direccion = self.lineEdit_7.text()
        provincia = self.lineEdit_8.text()
        canton = self.lineEdit_9.text()
        distrito = self.lineEdit_10.text()
        codigo_postal = self.lineEdit_12.text()
        numero = self.lineEdit_12.text()
        nombre_completo = self.lineEdit_5.text() + " " + self.lineEdit_6.text()

        if self.checkBox.isChecked(): 
            required_fields = [nombre, numeroDtarjeta, correo, vencimiento_tarjeta, ccv]     
        else:
            required_fields = [nombre, numeroDtarjeta, correo, vencimiento_tarjeta, ccv, direccion, provincia, canton, distrito, codigo_postal, numero, nombre_completo]
        if not all(required_fields):
            self.show_message("Completa todos los campos requeridos", "Error")
            return

        now = datetime.now()
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        numero_transaccion = random.randint(1000000, 9999999)
        articulos_comprados = [producto.to_dict() for producto in self.productos]

        # Crear el diccionario con los datos
        data = {
            "nombre": nombre,
            "correo": correo,
            "hora": fecha_hora,
            "numero_transaccion": numero_transaccion,
            "total": self.label_23.text(),
            "articulos_comprados": articulos_comprados
        }
        
        json_path = "C:/Datos1_Proyecto1/MyPetsCR/Interfaz/ComprasClientes.json"
        try:
            if os.path.exists(json_path):
                with open(json_path, "r", encoding='utf-8') as json_file:
                    existing_data = json.load(json_file)
            else:
                existing_data = []

            existing_data.append(data)

            with open(json_path, "w", encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, indent=4, ensure_ascii=False)

            self.show_message("Su pago fue procesado", "Pago Procesado")
        except Exception as e:
            logging.error(f"Error while writing purchase data: {e}")


    def show_message(self, message, title):
        QMessageBox.information(self, title, message)      
        
    def show_Errormessage(self, message, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

#CLASE PRINCIPAL
class Tienda(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        ui_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Tienda.ui"
        if not os.path.isfile(ui_file_path):
            raise FileNotFoundError(f"The file {ui_file_path} does not exist.")
        uic.loadUi(ui_file_path, self)
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.productos = []  # Inicializar la lista de productos
        self.loaddata()

        self.image = QtWidgets.QLabel(self)
        self.image.setGeometry(860, 350, 200, 200)
        self.image.setScaledContents(True)
        image_path = "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\mipet2.jpg"
        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            if not pixmap.isNull():
                self.image.setPixmap(pixmap)
    
        # click para conectar la imagen
        self.tableWidget.cellClicked.connect(self.showProductImage)
        self.selected_products = []

        self.pushButton_5.clicked.connect(self.show_selected_productos_list)
        self.pushButton_4.clicked.connect(self.show_login)
        self.pushButton.clicked.connect(self.show_main_window)

    def show_login(self):
        self.login_window = Login(self.main_window)
        self.login_window.show()
        self.close()

    def show_main_window(self):
        # Mostrar la ventana principal
        self.close()
    

    def show_selected_productos_list(self):
        if self.selected_products:
            self.productos_list = ProductosListView(self.selected_products, self.remove_product_from_selected)
            self.productos_list.show()
        else:
            self.showWarningMessage("No hay productos seleccionados.")

    def showProductImage(self, row, column):
        # Obtener el producto seleccionado
        producto = self.productos[row]
        image_path = producto.imagen
        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            if not pixmap.isNull():
                self.image.setPixmap(pixmap)
                print(f"Image {image_path} set for row {row}")
            else:
                print(f"Failed to load image from {image_path}")
        else:
            print(f"Image {image_path} not found")
      
    def loaddata(self):
        #esto agarra las cosas del archivo json
        json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Productos_Veterinaria (1).json"

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
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(producto.marca))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{producto.precio_final():.2f}"))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto.cantidad_disponible)))
            # Botón para comprar
            button = QPushButton("Agregar")
            button.clicked.connect(lambda checked, r=row: self.handleButtonClicked(r))
            self.tableWidget.setCellWidget(row, 4, button)

    def handleButtonClicked(self, row):
        product = self.productos[row]
        if product.cantidad_disponible > 0:
            product.cantidad_disponible -= 1
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(product.cantidad_disponible)))
            self.selected_products.append(product)
            self.updateCartLabel()
        else:
            self.showWarningMessage(f"No hay más stock disponible, pronto se hará restock!!")

    def process_payment(self):
        QMessageBox.information(self, "Pago Procesado", "El pago ha sido procesado con éxito.")
        for producto in self.productos:
            self.registrar_compra(producto)  # Registrar cada compra
        self.productos.clear()
        self.load_data(self.productos)
        self.update_total()

    def registrar_compra(self, product):
        nueva_compra = {
            'Factura': len(self.selected_products),  # Ejemplo: número de factura
            'Fecha': '2024-06-03',  # Ejemplo: fecha de compra
            'Cliente': 'Cliente Desconocido',  # Cambiar según el cliente
            'Productos Comprados': [product.descripcion],
            'Cantidad': 1,
            'Subtotal': product.precio,
            'Descuento': 0,
            'Total': product.precio,
            'Estado': 'Completado'
        }
        historial_compras = HistorialCompras()
        historial_compras.actualizar_historial(nueva_compra) # Revisar

    def showWarningMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle("Sin Stock")
        msg_box.setStyleSheet("QLabel { color : white }")
        msg_box.exec()

    def updateCartLabel(self):
        cart_count = len(self.selected_products)
        self.label_7.setText(f"{cart_count}")

    def remove_product_from_selected(self, producto):
        self.selected_products.remove(producto)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Tienda()
    window.show()
    sys.exit(app.exec())
