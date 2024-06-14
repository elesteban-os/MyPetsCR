from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from .NewExpe import ExpedienteDialog
from .Citas_Client import MainWindow
from .HistorialComprasAdmi import HistorialComprasAdmi
from .Tienda import Tienda

class ClienteWindow(QMainWindow):
    def __init__(self, main_window):
        self.main_window = main_window
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana5.ui", self)

        
        self.pushButton_6.clicked.connect(self.Expediente)
        self.pushButton_9.clicked.connect(self.CrearCita)
        self.pushButton_2.clicked.connect(self.show_historial)
        self.pushButton_4.clicked.connect(self.show_tienda)
        self.pushButton_5.clicked.connect(self.close_and_return)

    def CrearCita(self):
        self.crear_cita = MainWindow()
        self.crear_cita.show()
        
    def Expediente(self):
        self.expediente_mascota = ExpedienteDialog()
        self.expediente_mascota.show()

    def show_historial(self):
        self.historial_window = HistorialComprasAdmi()
        self.historial_window.show()

    def show_tienda(self):
        self.tienda_window = Tienda(self.main_window)
        self.tienda_window.show()

    def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close()
