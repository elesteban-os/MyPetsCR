import sqlite3

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from db.database import Database

class Login(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("ui/Ventana2.ui", self)
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.close_application)
        self.pushButton.clicked.connect(self.login_user)

    def close_application(self):
        self.close()

    def login_user(self):
        email = self.lineEdit.text().strip().lower()
        password = self.lineEdit_2.text().strip()
        selected_role = None

        if self.radioButton.isChecked():
            selected_role = "Administrador"
        elif self.radioButton_2.isChecked():
            selected_role = "Veterinario"
        elif self.radioButton_3.isChecked():
            selected_role = "Cliente"

        if not email or not password or not selected_role:
            QMessageBox.warning(self, "Login Failed", "Por favor llene todos los espacios en blanco y seleccione un rol")
            return

        if self.verify_user(email, password, selected_role):
            QMessageBox.information(self, "Login exitoso", f"Logueado como un {selected_role}")
            self.redirect_user(selected_role)
        else:
            QMessageBox.warning(self, "Login fallido", "Email, contraseña o rol incorrectos")

    def verify_user(self, email, password, role):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        if role == "Cliente":
            query = 'SELECT * FROM clientes WHERE LOWER(email) = ? AND contrasena = ? AND LOWER(tipo_usuario) = ?'
            cursor.execute(query, (email, password, role.lower()))
        else:
            query = 'SELECT * FROM personas WHERE LOWER(email) = ? AND contrasena = ? AND LOWER(tipo_usuario) = ?'
            cursor.execute(query, (email, password, role.lower()))

        user = cursor.fetchone()
        conn.close()

        return user is not None

    def redirect_user(self, role):
        if role == "Cliente":
            self.main_window.show_cliente_window()
        elif role == "Administrador":
            self.main_window.show_administrador_window()
        elif role == "Veterinario":
            self.main_window.show_veterinario_window()
        self.close()
