from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import sqlite3
from registrarUsuario import FormularioRegistro


class PaginaAdministrador(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("Ventana7.ui", self)


        # Conectar el botón de registrar usuario a la función para abrir el formulario de registro
        self.pushButton_1.clicked.connect(self.abrir_formulario_registro)
        self.pushButton_9.clicked.connect(self.close_and_return)

    def close_application(self):
        QApplication.quit()


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