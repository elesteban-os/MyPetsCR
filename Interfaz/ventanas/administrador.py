from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class AdministradorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana7.ui", self)


