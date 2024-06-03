import sys
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic
from .ProductosTienda import ProductosTienda

#se usa este archivo para manejar la parte de la interfaz del administrador pq la otra no estaba sirviendo para nada :))

class AdministradorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana7.ui", self)
        self.pushButton.clicked.connect(self.miau)
    
    def miau(self):
        self.productos_window = ProductosTienda()
        self.productos_window.show()


