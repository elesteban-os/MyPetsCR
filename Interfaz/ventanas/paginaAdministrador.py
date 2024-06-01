from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic
import sys
import sqlite3
from registrarUsuario import FormularioRegistro
from Citas import VentanaCitasAdmi

class PaginaAdministrador(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("Ventana7.ui", self)
        # Conectar el botón de registrar usuario a la función para abrir el formulario de registro
        self.pushButton_1.clicked.connect(self.abrir_formulario_registro)
        self.pushButton_9.clicked.connect(self.close_and_return)
        self.pushButton_8.clicked.connect(self.crear_cita)
        self.pushButton_5clicked.connect(self.añadir_productos)
    

    def close_application(self):
        QApplication.quit()

    def añadir_productos(self):
        self.ventana_productos = QWidget()
        self.ventana_productos.setWindowTitle("Añadir Producto")
        self.ventana_productos.setGeometry(150, 150, 400, 300)
        self.ventana_productos.show()
    

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

#if __name__ == "__main__":
   # app = QApplication(sys.argv)
   # window = PaginaAdministrador()
   # window.show()
   # sys.exit(app.exec())