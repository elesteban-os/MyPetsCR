import sys
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic
from .ProductosTienda import ProductosTienda

#se usa este archivo para manejar la parte de la interfaz del administrador pq la otra no estaba sirviendo para nada :))

class AdministradorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana7.ui", self)
        self.pushButton.clicked.connect(self.miau)
        # Conectar el botón de registrar usuario a la función para abrir el formulario de registro
        self.pushButton_1.clicked.connect(self.abrir_formulario_registro)
        self.pushButton_9.clicked.connect(self.close_and_return)

    def abrir_formulario_registro(self):
            self.formulario_registro = RegistrarUsuario(self)
            self.formulario_registro.show()

        def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close()
            
    def miau(self):
        self.productos_window = ProductosTienda()
        self.productos_window.show()


