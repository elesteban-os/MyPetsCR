from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QMessageBox
from PyQt6 import uic
import sys 
import re

from baseDatos import Database



class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        uic.loadUi("Ventana6.ui", self)

        # Conecta el botón de registro
        self.pushButton.clicked.connect(self.register_user)
        
        # Conecta el botón de cancelar
        self.pushButton_2.clicked.connect(self.close_and_return)


        # Inicializa la base de datos
        self.database = Database()

    def register_user(self):
        # Recopila los datos del formulario
        nombre = self.lineEdit.text()
        telefono = self.lineEdit_2.text()
        correo = self.lineEdit_3.text()
        contrasena = self.lineEdit_4.text()
        mascota = self.lineEdit_5.text()
        direccion = self.lineEdit_6.text()

        # Validación simple del formulario
        if not (nombre and telefono and correo and contrasena and mascota and direccion):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            QMessageBox.warning(self, "Error", "Correo electrónico no válido")
            return

        # Guardar en la base de datos
        self.database.add_user(nombre, telefono, correo, contrasena, mascota, direccion)

        QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente")
        self.close_and_return()


    def close_and_return(self):
        self.parent.show()
        self.close()
