from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
from .BuscarCliente import BuscarCliente
import sqlite3

class RegistrarMascota(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        uic.loadUi("Ventana9.ui", self)

        self.main_window = main_window
        self.pushButton.clicked.connect(self.registrar_mascota)
        self.pushButton_2.clicked.connect(self.cancelar_registro)
        self.pushButton_14.clicked.connect(self.abrir_buscar_cliente)
        # Añadir opciones al comboBoxEspecie
        self.comboBoxEspecie.addItems(["Canino", "Felino", "Ave", "Reptil", "Equino"])

    def abrir_buscar_cliente(self):
        buscar_cliente = BuscarCliente(self)
        buscar_cliente.exec()

    def registrar_mascota(self):
        nombre_mascota = self.lineEdit_8.text().strip()
        especie = self.comboBoxEspecie.currentText().strip()
        raza = self.lineEdit_10.text().strip()
        edad = self.lineEdit_11.text().strip()
        alergias = self.lineEdit_13.text().strip()
        padecimientos = self.lineEdit_14.text().strip()
        id_cliente = self.lineEdit_12.text().strip()

        # Validación de entradas
        if not (nombre_mascota and especie and raza and edad and alergias and padecimientos and id_cliente):
            QMessageBox.warning(self, "Registro fallido", "Por favor, complete todos los campos obligatorios.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()

        try:
            # Insertar datos en la tabla mascotas
            cursor.execute('''
                INSERT INTO mascotas (nombre, especie, raza, edad, alergias, padecimientos, id_cliente) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', (nombre_mascota, especie, raza, edad, alergias, padecimientos, id_cliente))

            # Obtener el id de la mascota recién insertada
            id_mascota = cursor.lastrowid

            # Insertar datos en la tabla expedientes
            cursor.execute('''
                INSERT INTO expedientes (id_mascota, nombre, especie, raza, edad, alergias, padecimientos) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', (id_mascota, nombre_mascota, especie, raza, edad, alergias, padecimientos))

            conn.commit()
            QMessageBox.information(self, "Registro exitoso", "Mascota registrada con éxito")
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error al registrar mascota: {str(e)}")

        finally:
            conn.close()

    def cancelar_registro(self):
        self.close()
        if self.main_window is not None:
            self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrarMascota()
    window.show()
    sys.exit(app.exec())
