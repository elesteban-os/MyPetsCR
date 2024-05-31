from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from db.database import Database

class RegistrarUsuario(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("ui/Ventana6.ui", self)
        self.main_window = main_window
        self.pushButton.clicked.connect(self.register_user)

    def register_user(self):
        nombre = self.lineEdit.text().strip()
        apellido = self.lineEdit_2.text().strip()
        tipo_usuario = self.comboBox.currentText()
        email = self.lineEdit_3.text().strip().lower()
        telefono = self.lineEdit_4.text().strip()
        direccion = self.lineEdit_5.text().strip()
        contrasena = self.lineEdit_6.text().strip()
        mascota = self.lineEdit_7.text().strip()

        if not (nombre and apellido and tipo_usuario and email and telefono and direccion and contrasena):
            QMessageBox.warning(self, "Registro fallido", "Por favor, complete todos los campos.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        if tipo_usuario.lower() == "cliente":
            cursor.execute('''
                INSERT INTO clientes (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena, mascota) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena, mascota))
        else:
            cursor.execute('''
                INSERT INTO personas (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "Registro exitoso", "Usuario registrado con éxito")
        self.close()
