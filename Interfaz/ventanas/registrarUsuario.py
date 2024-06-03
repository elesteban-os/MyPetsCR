from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QPushButton
from PyQt6 import uic
import sys
import sqlite3
from MostrarDatos import MostrarDatos



class FormularioRegistro(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        uic.loadUi("Ventana6.ui", self)

       # self.pushButton.clicked.connect(self.registrar_cliente)
        self.pushButton_2.clicked.connect(self.volver_a_pagina_administrador)

        self.initialize_comboBox_tipo_usuario()
        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.register_user)



    # Botón para abrir la ventana de mostrar datos
        self.pushButtonMostrarDatos = self.findChild(QPushButton, "pushButtonMostrarDatos")
        self.pushButtonMostrarDatos.clicked.connect(self.abrir_mostrar_datos)

    def abrir_mostrar_datos(self):
        self.mostrar_datos_window = MostrarDatos()
        self.mostrar_datos_window.show()


    def initialize_comboBox_tipo_usuario(self):
        self.comboBox_tipo_usuario = self.findChild(QComboBox, "comboBox_tipo_usuario")
        
        if self.comboBox_tipo_usuario is not None:
            self.comboBox_tipo_usuario.addItem("")  # Añadir un ítem vacío
            self.comboBox_tipo_usuario.addItems(["Administrador", "Cliente","Veterinario"])
        else:
            QMessageBox.critical(self, "Error", "No se encontró el QComboBox 'comboBox_tipo_usuario'.")


    def volver_a_pagina_administrador(self):
        if self.parent_window is not None:
            self.parent_window.show()
        self.close()


    def register_user(self):
        # Capturar los datos del formulario
        nombre = self.lineEdit.text().strip()
        apellido = self.lineEdit_5.text().strip()
        tipo_usuario = self.comboBox_tipo_usuario.currentText()
        email = self.lineEdit_3.text().strip().lower()
        telefono = self.lineEdit_2.text().strip()
        direccion = self.lineEdit_6.text().strip()
        contrasena = self.lineEdit_4.text().strip()

        # Validar que todos los campos estén llenos
        if not (nombre and apellido and tipo_usuario and email and telefono and direccion and contrasena):
            QMessageBox.warning(self, "Registro fallido", "Por favor, complete todos los campos.")
            return

        # Conectar a la base de datos e insertar los datos en la tabla correspondiente
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        try:
            if tipo_usuario == "Cliente":
                cursor.execute('''
                    INSERT INTO clientes (nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena) VALUES 
                    (?, ?, ?, ?, ?, ?, ?)
                ''', (nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena))
            else:
                cursor.execute('''
                    INSERT INTO personas (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena) VALUES 
                    (?, ?, ?, ?, ?, ?, ?)
                ''', (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena))

            conn.commit()
            QMessageBox.information(self, "Registro exitoso", "Usuario registrado con éxito")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al insertar en la base de datos: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioRegistro()
    window.show()
    sys.exit(app.exec())
