import sqlite3
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic
import sys

class MostrarDatos(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\VentanaMostrarDatos.ui", self)
        
        # Botón para cerrar la ventana
        self.pushButtonCerrar = self.findChild(QPushButton, "pushButtonCerrar")
        self.pushButtonCerrar.clicked.connect(self.close)
        
        # Botones para limpiar las tablas
        self.pushButtonLimpiarClientes = self.findChild(QPushButton, "pushButtonLimpiarClientes")
        self.pushButtonLimpiarClientes.clicked.connect(self.limpiar_tabla_clientes)
        
        self.pushButtonLimpiarPersonas = self.findChild(QPushButton, "pushButtonLimpiarPersonas")
        self.pushButtonLimpiarPersonas.clicked.connect(self.limpiar_tabla_personas)
        
        # Tablas para mostrar los datos
        self.tableWidgetClientes = self.findChild(QTableWidget, "tableWidgetClientes")
        self.tableWidgetPersonas = self.findChild(QTableWidget, "tableWidgetPersonas")
        
        # Cargar los datos
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        # Cargar datos de la tabla clientes
        cursor.execute("SELECT nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena FROM clientes")
        rows_clientes = cursor.fetchall()
        self.tableWidgetClientes.setRowCount(len(rows_clientes))
        self.tableWidgetClientes.setColumnCount(len(rows_clientes[0]) if rows_clientes else 0)
        self.tableWidgetClientes.setHorizontalHeaderLabels(["Nombre", "Apellido", "Teléfono", "Dirección", "Tipo Usuario", "Email", "Contraseña"])

        for row_idx, row_data in enumerate(rows_clientes):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidgetClientes.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        # Cargar datos de la tabla personas
        cursor.execute("SELECT nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena FROM personas")
        rows_personas = cursor.fetchall()
        self.tableWidgetPersonas.setRowCount(len(rows_personas))
        self.tableWidgetPersonas.setColumnCount(len(rows_personas[0]) if rows_personas else 0)
        self.tableWidgetPersonas.setHorizontalHeaderLabels(["Nombre", "Apellido", "Tipo Usuario", "Email", "Teléfono", "Dirección", "Contraseña"])

        for row_idx, row_data in enumerate(rows_personas):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidgetPersonas.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        conn.close()

    def limpiar_tabla_clientes(self):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM clientes")
            conn.commit()
            QMessageBox.information(self, "Éxito", "Tabla 'clientes' limpiada exitosamente.")
            self.load_data()  # Recargar los datos para reflejar los cambios
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al limpiar la tabla 'clientes': {e}")
        finally:
            conn.close()

    def limpiar_tabla_personas(self):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM personas")
            conn.commit()
            QMessageBox.information(self, "Éxito", "Tabla 'personas' limpiada exitosamente.")
            self.load_data()  # Recargar los datos para reflejar los cambios
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al limpiar la tabla 'personas': {e}")
        finally:
            conn.close()
