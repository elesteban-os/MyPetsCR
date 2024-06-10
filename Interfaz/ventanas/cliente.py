from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from .NewExpe import ExpedienteDialog

class ClienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana5.ui", self)

        
        self.pushButton_6.clicked.connect(self.Expediente)
        print("pushButton_6 connected")

    def Expediente(self):
        self.expediente_mascota = ExpedienteDialog()
        self.expediente_mascota.show()
