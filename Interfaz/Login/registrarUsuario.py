from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QMessageBox
from PyQt6 import uic
import sys 
import re
import sqlite3

#from Login import Login



class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        uic.loadUi("Ventana6.ui", self)

        # Conecta el botón de registro
        self.pushButton.clicked.connect(self.register_user)
        
        # Conecta el botón de cancelar
        self.pushButton_2.clicked.connect(self.close_and_return)

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
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                telefono TEXT,
                correo TEXT,
                contrasena TEXT,
                mascota TEXT,
                direccion TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO users (nombre, telefono, correo, contrasena, mascota, direccion)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, telefono, correo, contrasena, mascota, direccion))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente")
        self.close_and_return()

    def close_and_return(self):
        if self.parent is not None:
            self.parent.show()
        self.close()
