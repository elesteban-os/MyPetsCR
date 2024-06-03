from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic
import sys
import sqlite3
from registrarUsuario import FormularioRegistro
from Citas import VentanaCitasAdmi

#este archivo nunca se usa y para nada sirve tambien entonces se usó el otro
#(no sé pq habían 2 la vdd pero el otro archivo era el que estaba conectado a main entonces ajá)

class PaginaAdministrador(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana7.ui", self)
        

        print("UI loaded")
        
        try:
            self.pushButton_1.clicked.connect(self.abrir_formulario_registro)
            print("pushButton_1 connected")
            self.pushButton_9.clicked.connect(self.close_and_return)
            print("pushButton_9 connected")
            self.pushButton_8.clicked.connect(self.crear_cita)
            print("pushButton_8 connected")
            self.pushButton_5.clicked.connect(self.añadir_productos)
            print("pushButton_5 connected")  # Corrección aquí
        except AttributeError as e:
            print(f"Error connecting buttons: {e}")

    def close_application(self):
        QApplication.quit()

    def añadir_productos(self):
        print("Hola")
        self.ventana_productos = QWidget()
        self.ventana_productos.setWindowTitle("Añadir Producto")
        self.ventana_productos.setGeometry(150, 150, 400, 300)
        self.ventana_productos.show()

    def abrir_formulario_registro(self):
        print("Abrir formulario de registro")

    def close_and_return(self):
        print("Cerrar y regresar")

    def crear_cita(self):
        print("Crear cita")
    def crear_cita(self):
         self.crear_cita = VentanaCitasAdmi()
         self.crear_cita.show()
         

    def abrir_formulario_registro(self):
            self.formulario_registro = FormularioRegistro(self)
            self.formulario_registro.show()

    def close_and_return(self):
        if self.parent() is not None:
            self.parent().show()
        self.close()   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaginaAdministrador()
    window.show()
    sys.exit(app.exec_())