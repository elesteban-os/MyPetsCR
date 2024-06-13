from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from .NewExpe import ExpedienteDialog
from .Citas_Client import MainWindow

class ClienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana5.ui", self)

        
        self.pushButton_6.clicked.connect(self.Expediente)
        print("pushButton_6 connected")
        self.pushButton_9.clicked.connect(self.CrearCita)
        print("pushButton_9 connected")

    def CrearCita(self):
        self.crear_cita = MainWindow()
        self.crear_cita.show()
        
    def Expediente(self):
        self.expediente_mascota = ExpedienteDialog()
        self.expediente_mascota.show()
