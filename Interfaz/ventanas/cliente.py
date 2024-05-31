from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class ClienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana5.ui", self)

