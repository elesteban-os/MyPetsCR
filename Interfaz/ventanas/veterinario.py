from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class VeterinarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana8.ui", self)
