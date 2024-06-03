import json
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6 import QtGui

#se crea esata clase para agregar productos a la tienda por parte del admin
class ProductosTienda(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\ProductosTienda.ui", self)
        self.file_n = ""

        self.pushButton.clicked.connect(self.browsefiles)
        self.pushButton_2.clicked.connect(self.addToDb)

    def browsefiles(self):
        file_tuple = QFileDialog.getOpenFileName(self, "Open file", "Desktop", "Image Files (*.jpg *.jpeg *.png)")
        self.file_n = file_tuple[0] 

        if self.file_n:
            pixmap = QtGui.QPixmap(self.file_n)
            self.label_8.setPixmap(pixmap)
        
    def addToDb(self):
        if (self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and
            self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text() and
            self.file_n):
            new_data = {
                'Código': self.lineEdit.text(),
                'Descripción': self.lineEdit_2.text(),
                'Marca': self.lineEdit_3.text(),
                'Precio': float(self.lineEdit_4.text()),
                'IVA': int(13),
                'CantidadDisponible': int(self.lineEdit_5.text()),
                'Categoría': self.lineEdit_6.text(),
                'Imagen': self.file_n
            }
            json_file_path = r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Productos_Veterinaria (1).json"
            try:
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
            except FileNotFoundError:
                data = []

            data.append(new_data)
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

            print(f"Data written to {json_file_path}")
        else:
            QMessageBox.warning(self, "Cuidado!", "LLena todos los espacios por favor (✿◠‿◠)")




