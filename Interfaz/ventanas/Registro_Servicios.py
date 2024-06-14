import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from PyQt6 import uic

class RegistroServicios(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Registro_Servicios.ui", self)

        # Conectar botones a funciones
        self.btn_agregar.clicked.connect(self.mostrarMensaje)
        self.btn_salir.clicked.connect(self.salirVentana)

    def mostrarMensaje(self):
        QMessageBox.information(self, "Mensaje", "¡Agregado correctamente!")

    def salirVentana(self):
        self.close()
