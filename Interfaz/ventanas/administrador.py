from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from .Citas_Admi import MainWindow
from .registrarUsuario import FormularioRegistro
from.EdiciónDeProductos import VentanaAdmin
from .HistorialCompras import HistorialCompras
from .RegistroMascota import RegistrarMascota
from .BuscarMascota import BuscarMascota
from .NewExpe import ExpedienteDialog
from .HistorialComprasAdmi import HistorialComprasAdmi
from .Facturacion import Facturacion

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
        self.pushButton_6.clicked.connect(self.facturacion)
        
        self.pushButton_10.clicked.connect(self.Expediente)
        print("pushButton_10 connected")
    
        self.pushButton_11.clicked.connect(self.CrearFacturaciones)
    
    def CrearFacturaciones(self):
        self.crear_facturacion = HistorialComprasAdmi()
        self.crear_facturacion.show()

    def Expediente(self):
        self.expediente_mascota = ExpedienteDialog()
        self.expediente_mascota.show()
        
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
        self.crear_cita = MainWindow()
        self.crear_cita.show()
        
    def productosTienda(self):
        self.edicion_window = VentanaAdmin()
        self.edicion_window.show()
        
    def facturacion(self):
        self.facturacion_window = Facturacion()
        self.facturacion_window.show()

    def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close() 
