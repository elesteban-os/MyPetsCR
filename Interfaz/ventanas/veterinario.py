from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from .ExpedienteVet import ExpedienteDialog
from .BuscarMascota import BuscarMascota

class VeterinarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana8.ui", self)

        self.pushButton_6.clicked.connect(self.expedienteVeterinario)

        self.pushButton_5.clicked.connect(self.close_and_return)

        self.push_Button_BuscarMascota.clicked.connect(self.buscarMascota)

    def buscarMascota(self):
        self.buscar_mascota = BuscarMascota(self)
        self.buscar_mascota.show()

    def expedienteVeterinario(self):
        self.expediente_mascota = ExpedienteDialog()
        self.expediente_mascota.show()


    def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close()
