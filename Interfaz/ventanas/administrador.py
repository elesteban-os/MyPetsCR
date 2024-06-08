import sys
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic

from .Citas import VentanaCitasAdmi
from .registrarUsuario import FormularioRegistro
from .ProductosTienda import ProductosTienda
from .HistorialCompras import HistorialCompras
from .RegistroMascota import RegistrarMascota
from .BuscarMascota import BuscarMascota

#se usa este archivo para manejar la parte de la interfaz del administrador pq la otra no estaba sirviendo para nada :))

class AdministradorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana7.ui", self)
        self.pushButton_8.clicked.connect(self.crear_cita)
        self.pushButton.clicked.connect(self.productosTienda)
        self.pushButton_9.clicked.connect(self.close_and_return)
        self.pushButton_1.clicked.connect(self.abrir_ventana_administrador)
        self.pushButton_7.clicked.connect(self.HistorialFacturaciones)
        self.pushButton_2.clicked.connect(self.registrarMascota)
        self.pushButtonBuscarMascota.clicked.connect(self.BuscarMascota)
    
    
    def BuscarMascota(self):
        self.buscar_mascota = BuscarMascota(self)
        self.buscar_mascota.show()

    def registrarMascota(self):
        self.registrar_mascota = RegistrarMascota(self)
        self.registrar_mascota.show()
    
    
    def HistorialFacturaciones(self):
        self.historialcompras = HistorialCompras(self)
        self.historialcompras.show()
    
    def abrir_ventana_administrador(self):
            self.formulario_registro = FormularioRegistro(self)
            self.formulario_registro.show()
    def crear_cita(self):
        print("Crear cita")

    def crear_cita(self):
         self.crear_cita = VentanaCitasAdmi()
         self.crear_cita.show()
        
    def productosTienda(self):
        self.productos_window = ProductosTienda()
        self.productos_window.show()
        
    def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close() 

